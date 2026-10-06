from pathlib import Path
import math, re, json, html
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
OUT=Path('/home/morgan/Desktop/Untitled Folder/courses/ZombieInvasionPrep/ZombieInvasionPrep/classes/field_assignments/files/sandbag-emergency-logistics')
# All quantities below are deliberately supplied classroom estimates, not engineering designs.
sc=[]
def add(title,kind,situation,mission,site,workers,shovels,equipment,bags,fill,materials,weather,deadline,constraint,n,reason,extra,arrival=0):
 sc.append(dict(id=len(sc)+1,title=title,kind=kind,situation=situation,mission=mission,site=site,workers=workers,shovels=shovels,equipment=equipment,bags=bags,fill=fill,materials=materials,weather=weather,deadline=deadline,constraint=constraint,n=n,reason=reason,extra=extra,arrival=arrival))
add('Hillside Library Entrance','Straightforward • diversion','Thunderstorm runoff is crossing a library forecourt below a steep Pittsburgh hillside.','Estimate a narrow two-layer diversion line leading runoff to an approved grass swale.','24 ft total line, including returns; filling point 40 ft away on level pavement.',8,4,'1 wheelbarrow; 1 radio',120,2,'One 10 × 30 ft plastic sheet; 6 cones','68°F; rain expected; daylight',3,'A 6 ft accessible entrance must stay open. The supplied 24 ft route avoids it.',48,'Reasonable for shallow runoff only. Verify the receiving swale remains safe.','Plastic apron, cones, accessible route and runoff observation')
add('Creekside Community Center','Moderate • shallow barrier','A slow creek rise may send shallow water toward a community center.','Estimate a broad three-layer barrier along the exposed side.','36 ft total length, including returns; fill 120 ft away; approved crest 9 in; forecast water 6 in.',12,6,'2 wheelbarrows; 2 radios',300,4,'Two 10 × 25 ft plastic sheets; tape; 8 cones','60°F; showers; daylight',4,'Do not ring the entire building or trap rainwater. Staff can relocate activities.',216,'Conditional: shallow, slow water only; leakage and drainage still matter.','Plastic overlap, drainage plan, relocation trigger')
add('Shelter Accessible Entry','Straightforward • diversion','A school shelter has runoff flowing across its main walkway.','Plan two narrow two-layer lines along the walkway edges.','Two 18 ft lines; fill 60 ft away; walkway 6 ft wide remains clear.',8,2,'1 utility cart; 1 radio',100,2,'Two 6 × 20 ft plastic sheets; 6 cones','72°F; rain; daylight',2,'The entrance is occupied. Work must not create a trip hazard.',72,'Reasonable if approved drainage carries water away without crossing the entrance.','Accessible detour during work, signs, plastic apron')
add('Communications Trailer','Moderate • equipment diversion','A county communications trailer is operating in a low parking area.','Plan a U-shaped narrow two-layer line around the uphill side and ends.','Trailer 16 × 8 ft; U has one 16 ft side and two 8 ft ends; fill 100 ft away.',8,4,'1 wheelbarrow; 2 radios',100,2,'One 20 × 20 ft sheet; 6 cones','70°F; storm approaching',2,'Leave the downhill side open. Keep vents, cables and evacuation routes clear.',64,'Useful as partial protection; move the trailer if the site starts flooding.','Cable protection, plastic apron, equipment relocation plan')
add('Utility Cabinet on a Hill','Short deadline • diversion','Runoff from a steep street is approaching a closed utility cabinet.','Plan an L-shaped narrow two-layer diversion line; utility staff handle the cabinet.','L legs 12 ft and 8 ft; fill 80 ft away.',4,2,'No cart; 1 radio',60,1,'One 10 × 15 ft sheet; 4 cones','65°F; rain within 45 minutes',0.75,'Workers must stay outside the utility exclusion zone. Nobody touches electrical equipment.',40,'Conditional: utility approval and isolation first; retreat if water enters exclusion zone.','Utility coordination, cones, plastic, relocation or isolation')
add('Fire Station Apron','Moderate • drainage','A damaged drain is sending runoff toward a fire station bay.','Plan a narrow two-layer line to a separate functioning inlet.','48 ft route includes returns and avoids the bay exit; fill 180 ft away.',12,4,'2 utility carts; 2 radios',140,2,'One 10 × 60 ft sheet; 10 cones','58°F; steady rain',3,'Emergency vehicles need a 14 ft exit. Never cover either drain with bags.',96,'Reasonable only if public works confirms inlet capacity and destination.','Traffic control, plastic, protected inlet and apparatus access')
add('Broken Drain at a School','Equipment shortage • drainage','A schoolyard inlet has collapsed after heavy rain.','Plan a narrow two-layer line toward a functioning grass drainage channel.','60 ft route; fill 200 ft away along a level path.',12,2,'1 wheelbarrow; 1 radio',150,2,'One 10 × 70 ft sheet; 8 cones','74°F; humid; showers',4,'Only two shovels serve three teams. Keep children out of the work area.',120,'Useful temporary diversion; more people cannot solve shovel and cart limits.','Fencing/cones, plastic, public works repair request')
add('Water-Main Break','Moderate • utility runoff','A water-main break is sending shallow water across an EMS supply-room entrance.','Estimate a narrow two-layer diversion line while utility crews shut off the main.','30 ft line to an approved surface channel; fill 90 ft away.',8,4,'1 utility cart; 2 radios',100,2,'One 10 × 40 ft sheet; 6 cones','50°F; daylight',1.5,'Do not approach undermined pavement. Source control may finish before bagging.',60,'Only a temporary supplement to shutoff, exclusion and professional inspection.','Utility contact, cones, plastic, supply relocation')
add('EOC Generator Pad','Moderate • equipment protection','An emergency operations site generator is receiving shallow hillside runoff.','Estimate a U-shaped narrow two-layer diversion line.','Pad 10 × 8 ft; U uses 10 + 8 + 8 ft; fill 150 ft away.',8,4,'1 wheelbarrow; 2 radios',100,2,'One 15 × 20 ft sheet; 6 cones','82°F; humid; thunderstorms',2,'Fueling access, exhaust clearance and manufacturer clearances must remain open.',52,'Useful only as approved runoff diversion; unsafe electrical conditions stop work.','Operator approval, plastic apron, isolation and relocation options')
add('Basement Window Wells','Straightforward • targeted protection','Shallow runoff is collecting at three community-building window wells.','Plan one broad three-layer U around each well.','Each U: 4 ft front plus two 2 ft returns; total three wells; fill 50 ft away.',8,4,'1 utility cart; 1 radio',180,3,'Three 8 × 8 ft sheets; tape','62°F; light rain',3,'Do not seal building ventilation or obstruct emergency exits.',144,'Targeted protection can be reasonable; seepage and internal water still require monitoring.','Plastic, building inspection, drainage and safe pumping by adults')
add('Long Riverfront Frontage','Resource shortage • shallow barrier','A riverfront storage site requests bags along a long exposed frontage.','Estimate the requested broad three-layer barrier, then decide whether to scale back.','480 ft total approved line; crest 9 in; forecast shallow water 6 in; fill 300 ft away.',16,8,'2 wheelbarrows; 1 pickup; 2 radios',400,6,'Four 10 × 50 ft sheets; 12 cones','55°F; rain; daylight',4,'Relocation trucks can move the critical inventory. This is not a deep-river levee design.',2880,'Wrong primary plan at this scale: bag shortage, sheet shortage and deadline favor relocating inventory.','Inventory priority list, evacuation/relocation, targeted protection')
add('Low Road Crossing','Reject or redesign • road access','A low road is forecast to have 18 in of moving water. Someone proposes a sandbag wall.','Estimate the requested structure, then evaluate safe alternatives.','Requested 120 ft broad four-layer line; modeled crest only 12 in; fill 100 ft away.',12,6,'2 wheelbarrows; 1 pickup; 2 radios',800,12,'Two 10 × 60 ft sheets; 16 cones; road-closure signs','Storm forecast; visibility worsening',2,'Emergency access must use a dry detour. No one may work in moving water.',1200,'Reject: modeled wall lower than water, moving water, roadway hazards and a short deadline.','Road closure, dry detour, public works and responder coordination')
add('Park Trail Washout','Straightforward • erosion','A park trail edge lost soil during a storm.','Estimate three approved small check structures on dry, firm ground upslope of the damage.','Each structure 8 ft long, two bags across and two layers; fill 160 ft away.',8,4,'1 wheelbarrow; 1 radio',120,2,'Three 6 × 10 ft filter-fabric pieces; 8 cones','64°F; dry; daylight',4,'Public works marked the locations. Keep the damaged trail closed.',96,'Useful temporary runoff control; bags do not rebuild the trail or carry people.','Filter fabric, closure signs and permanent repair')
add('Road Shoulder After a Storm','Moderate • stabilization','Runoff is washing fine soil from a closed road shoulder.','Estimate an approved small erosion-control line above the damaged area.','30 ft line, two bags across and two layers; fill 250 ft away.',12,6,'2 wheelbarrows; 2 radios',150,2,'One 8 × 40 ft filter-fabric strip; 12 cones','59°F; dry',3,'Closed road stays closed. Bags provide no structural support for vehicles.',120,'Temporary surface protection only; public works must assess the road before reopening.','Filter fabric, barricades, engineering inspection')
add('Landslide at a Hillside Street','Reject or redesign • slope','Cracks and a small slide appear above a hillside street. A resident requests bags to hold the slope.','Estimate four proposed erosion-control lines, then assess whether they solve the hazard.','Four lines, each 25 ft long, two bags across and two layers; fill 200 ft away outside exclusion zone.',8,4,'1 wheelbarrow; 2 radios',500,7,'Four 8 × 30 ft filter-fabric strips; 12 cones','Wet slope; more rain forecast',3,'Nobody enters the slide zone. Public works and a slope specialist are requested.',400,'Reject as slope support. Surface-control estimates do not establish landslide stability.','Exclusion, road closure, utility checks and professional slope assessment')
add('Small Culvert Approach','Moderate • drainage and erosion','Runoff is eroding a closed culvert approach while a repair crew is en route.','Plan two approved erosion-control lines above the damaged approach.','Two 15 ft lines, two bags across and two layers; fill 220 ft away.',8,4,'1 wheelbarrow; 1 radio',150,2,'Two 8 × 20 ft filter-fabric strips; 8 cones','61°F; showers',4,'Do not narrow the culvert opening. Crew arrives after the deadline.',120,'Partial solution: retain access restrictions and avoid backing water upstream.','Filter fabric, exclusion, culvert inspection and repair')
add('Creek Bank Beside a Ballfield','Limited workers • erosion','A closed ballfield has a small creek-bank scour area.','Estimate three approved erosion-control lines on dry ground set back from the bank.','Three 12 ft lines, two bags across and two layers; fill 280 ft away.',4,2,'1 wheelbarrow; 1 radio',180,3,'Three 8 × 15 ft filter-fabric strips; 10 cones','70°F; dry',4,'Only one team. No work at the unstable edge or in the creek.',144,'Conditional temporary runoff control; bank repair requires qualified crews.','Filter fabric, closure and professional bank stabilization')
add('Shelter Cleaning-Water Basin','Moderate • non-potable basin','A shelter needs a temporary rainwater collection area for adult-managed cleaning.','Estimate a lined rectangular basin perimeter and a sensible operating volume.','Inside 12 × 8 ft; two-bag-wide, two-layer berm; proposed operating depth 0.5 ft; fill 80 ft away.',8,4,'1 utility cart; 1 radio',200,3,'One intact 24 × 20 ft liner; non-potable signs; 6 cones','68°F; rain forecast',4,'Flat ground only; no guaranteed rainfall. Authorized maximum 0.5 ft depth. Keep people out.',160,'Conditional: lined, supervised, ground-level non-potable collection; water safety and availability govern.','Liner, labels, barriers, overflow route and adult draw-off plan')
add('Oversized Rainwater Request','Reject or redesign • basin','A shelter asks for a deep rainwater basin on a paved lot.','Estimate requested perimeter and volume; propose a smaller or different storage method.','Inside 30 × 20 ft; four-bag-wide, four-layer berm; requested depth 2 ft; fill 300 ft away.',12,6,'2 wheelbarrows; 1 pickup; 2 radios',500,8,'One 20 × 20 ft liner; 12 cones','80°F; humid; storm soon',6,'Classroom four-layer crest is 1 ft. No approved deep-basin design; liner cannot cover the base.',1600,'Reject: requested depth exceeds berm, undersized liner, enormous water load and insufficient bags.','Approved tanks/containers, water delivery, smaller shallow basin with approval')
add('Clinic Sanitation Collection','Transportation problem • basin','A temporary clinic needs an adult-managed non-potable water reserve.','Estimate a lined square basin perimeter and operating volume.','Inside 10 × 10 ft; two-bag-wide, two-layer berm; depth 0.25 ft; fill 300 ft away via dry level route.',8,4,'1 wheelbarrow only; 2 radios',180,3,'One 22 × 22 ft liner; 6 cones; non-potable signs','63°F; light rain',3,'No carts or vehicles fit the route. Collected water is not for drinking or handwashing.',160,'Conditional: movement is likely limiting; delivered approved containers may be easier.','Liner, signage, barrier, overflow and authorized sanitation-use plan')
add('Shelter Tarp Floor','Straightforward • temporary infrastructure','A dry shelter staging area needs a plastic ground cover held against light wind.','Estimate bags spaced around the ground-cover perimeter using the anchor rule.','Cover 20 × 12 ft; one bag every 4 ft of perimeter; fill 60 ft away.',4,2,'1 utility cart; 1 radio',50,1,'One 20 × 12 ft tarp; 6 cones','66°F; light wind; dry',2,'This is a ground cover only. Keep bags away from accessible walking routes.',16,'Reasonable in light wind on dry ground; do not infer structural anchoring strength.','Tarp, edge markings and trip-hazard control')
add('Temporary Privacy Partitions','Straightforward • temporary infrastructure','A shelter needs privacy screens on an approved indoor frame system.','Estimate requested bags at base stations, then check supervisor approval.','Six approved base stations; two bags at each; fill 80 ft from entrance.',4,2,'1 utility cart; 1 radio',40,1,'Six rated frames and screens; floor protection','Indoor use; dry route',2,'Bags are only approved supplementary ballast. No free-standing bag wall; exits stay open.',12,'Reasonable only with the supplied rated system and supervisor-approved ballast.','Rated frames, floor protection, accessible egress and supervisor check')
add('Mobile Charging Tent','Moderate • temporary infrastructure','A shelter requests supplementary ballast for an approved charging tent.','Estimate bags specified by the site supervisor at approved stations.','Eight stations with four bags each; fill 150 ft away.',8,4,'1 utility cart; 2 radios',80,2,'One rated tent with its required anchors; cable covers; 8 cones','76°F; light wind now; thunderstorms later',2,'Actual tent anchoring follows manufacturer instructions; bag count is not a wind rating.',32,'Conditional supplement only. Suspend use and shelter indoors for threatening weather.','Rated anchors, cable covers, electrical supervision and weather shutdown')
add('Emergency Wayfinding Signs','Limited equipment • signage','Temporary signs are needed at an emergency assistance site.','Estimate approved supplementary base ballast at each sign.','Ten approved signs, two bags per sign; placements along 600 ft pedestrian route; fill at midpoint.',8,2,'1 utility cart; 2 radios',60,1,'Ten rated sign stands; reflective signs; floor/ground protection','45°F; dusk begins in one hour',1.5,'Only two shovels; route stays accessible. No improvised overhead supports.',20,'Reasonable with approved stands; distributed placement and visibility may dominate.','Reflective signage, rated stands, lights if work continues')
add('Debris-Sorting Tarp','Moderate • temporary infrastructure','Public works is sorting clean storm debris on a closed paved area.','Estimate bags to hold down an empty tarp before sorting begins.','Tarp 40 × 20 ft; one bag every 4 ft around perimeter; fill 200 ft away.',8,4,'1 wheelbarrow; 1 radio',80,2,'One 40 × 20 ft tarp; 10 cones; caution tape','58°F; breezy; daylight',2,'No sharp debris goes onto the tarp until adult crews approve it. Ballast is not containment.',30,'Reasonable for temporary ground-cover edging; sorting and debris disposal remain separate.','Tarp, exclusion, labeled sorting zones and removal plan')
add('Potentially Contaminated Runoff','Planning only • containment','Responders report runoff from an unknown spill approaching a storm inlet.','Estimate an approved narrow three-layer diversion line on the clean side, subject to responder authorization.','50 ft line to a responder-designated containment area; fill 100 ft away in clean zone.',8,4,'1 wheelbarrow; 2 radios',180,3,'One 10 × 60 ft sheet; 12 cones; caution tape','60°F; rain in one hour',1,'Unknown material. Ordinary gloves and glasses do not authorize entry; no student handles hazards.',150,'Conditional on hazardous-material responder direction; source control and drain protection may be better.','Responder-specified PPE, compatible liner, exclusion, collection/disposal')
add('Flooded Maintenance Yard','Planning only • contaminated water','Water from a maintenance yard may contain oil and other contaminants.','Estimate a broad three-layer line along a clean-side boundary, then assess deployment.','80 ft total approved line; fill 250 ft away on dry clean pavement.',12,6,'2 wheelbarrows; 2 radios',300,4,'One 10 × 100 ft sheet; 14 cones; caution tape','57°F; rain; fading daylight',2,'Only trained responders decide liner compatibility and handling; no discharge to drains.',480,'Requested bags and fill exceed supply; prioritize isolation, professional recovery and a shorter approved segment.','Hazmat coordination, compatible liner, lights, disposal and exclusion')
add('Sand Delivery on a Closed Hill','Transportation problem • diversion','A school on a steep street needs diversion, but the sand truck cannot climb the closed route.','Plan a narrow two-layer line and account for last-mile fill delivery.','90 ft line; alternate fill staging 600 ft away; dry but uphill pedestrian route.',12,6,'2 wheelbarrows; 1 pickup (dry detour only); 2 radios',220,0,'One 10 × 100 ft sheet; 8 cones; supplier offers 3 yd³','73°F; dry now; rain later',4,'Supplier reaches alternate staging after 1 h. Transfer from there must be planned; cycle times are optimistic on hills.',180,'Useful if last-mile transfer can finish; choose a closer approved fill site or mechanized transfer.','Delivery plan, sheet, route control, rest and additional transfer capacity',arrival=1)
add('Overnight Supply Depot','Long operation • shallow barrier','A dry supply depot has time to protect one exposed side before a forecast shallow rise.','Estimate a broad three-layer barrier and a sustained overnight staffing plan.','120 ft total line; approved crest 9 in, forecast water 6 in; fill 240 ft away.',16,8,'2 wheelbarrows; 1 pickup; 2 radios; work lights',900,12,'Three 10 × 50 ft sheets; tape; 12 cones','48°F; drizzle; work extends into darkness',12,'A 4 yd³ dump delivery arrives after 2 h; only 6 yd³ is on site initially. Lamps need verified power.',720,'Conditional; rotation, food, lighting and delivery staging are as important as bags.','Sheets, powered lights, meals, warm breaks, staged fill and relief workers',arrival=0)
add('Two Sites, One Workforce','Resource allocation • prioritization','A shelter entrance and an empty recreation building both request protection.','Estimate both requests, choose priorities and schedule the shared workforce.','Shelter: 30 ft narrow two-layer line. Recreation building: 60 ft broad three-layer line. Fill 100 ft from shelter and 400 ft from recreation site.',12,4,'1 utility cart; 1 pickup; 2 radios',350,5,'One 10 × 40 ft sheet; one 10 × 70 ft sheet; 12 cones','69°F; storms approaching',3,'Shelter deadline 1 h; recreation deadline 3 h. Additional bags unavailable. People take priority over empty property.',420,'Combined plan exceeds bag/fill stock; prioritize shelter, reduce or abandon second request.','Priority communication, separate deadlines, accessible shelter entrance and phased allocation')
questions='''Student Planning Questions
Use the common worksheet and your team's measured rate. Answer all 17 prompts: bags; fill; four-person teams; team-hours; elapsed time; tools; shovels; PPE; fill delivery; filled-bag movement; bottleneck; drinking water; food; rest/rotation; other materials; practicality; and changes needed. Show your sketch, calculations, assumptions and priority decision. For a basin, also calculate volume, gallons, approximate water load and a sensible operating limit.'''
part1=[('PART 1 • THE 20-MINUTE EXPERIMENT', '''Zombie Invasion Prep • Sandbag Emergency Logistics
Student calculation packet • One copy per team, plus reference pages for each student

The challenge
With four workers, fill, close, carry and place as many acceptable sandbags as you safely can in 20 minutes. More empty bags may be supplied if the teacher has them. Completed means all four steps are finished at the marked destination. A partly filled bag or a bag still waiting to move does not count.

Before the clock starts
Put on work gloves and safety glasses. Listen to the teacher's demonstration and match the sample bag: about half to two-thirds full, flexible and comfortable to handle. Close it using the teacher's consistent demonstrated method. Real flood barriers often use folded/tucked tops rather than tied bags; this class uses the same closure for everyone. Do not pack bags solid or compete by making tiny bags.
Choose roles: hold/fill, shovel, close, move/place. You may change roles. Keep shovel swing zones and the carry path clear. Lift comfortably, use a buddy when needed, walk, and put bags down under control. Stop for pain, fatigue or unsafe conditions.

Timing and counting
Teacher gives one start signal and a hard stop at 20 minutes. Count only bags accepted at the destination at the stop. Work safely; this is a measurement, not a speed contest. Do not empty and refill a bag during the trial. Count each bag once.

If the supply runs out
Record the time you ran out and stop counting. Do not quietly report a full 20-minute maximum. A 20-minute count × 3 is still the observed output under the supply limit; it underestimates unrestricted production. Ask the teacher how to label and use this limited trial. If you produced zero, record the bottleneck; a zero rate cannot be used as a divisor.

Safety agreement
We work only with clean sand on a teacher-inspected dry practice site. We do not build live flood barriers or enter floodwater. We keep eyewear on, wear closed-toe footwear, avoid throwing sand and wash hands before eating. The teacher may stop the trial for weather or any hazard. Report an injury immediately.

Name / team: __________________________________________
Four team members: ___________________________________
Date / trial location: ___________________________________
Teacher-approved destination and carry route: ______________'''),
('TEAM DATA & BASIC CALCULATIONS', '''Names: __________________________  Team: __________

Record what happened
Workers: 4      Trial duration: 20 minutes
Completed bags at final location, B: ______________________
Approximate one-way carrying distance: __________ ft
Shovels used: ______   Other moving equipment: ____________
Was the full trial supplied with empty bags and sand? Yes / No
If not, when and what ran out? ___________________________
Weather / ground / route conditions: _____________________
Closure / fill standard used: _____________________________
Jobs at the start and any changes:
____________________________________________________
____________________________________________________
Main bottleneck and evidence (waiting, queues, crowded area):
____________________________________________________
____________________________________________________

1. Experimental team production rate
R = B × 3 = ______ × 3 = ______ bags per team-hour
This means one team of four at the conditions you measured.

2. Experimental average per person
R ÷ 4 = ______ ÷ 4 = ______ bags per person-hour
This is an average within the team, not a promise that a solo worker can do every job at this rate.

3. Fill represented by the completed bags
B ÷ 75 = ______ ÷ 75 = ______ cubic yards of fill (estimate)
No weighing. We use the same 75 bags ≈ 1 yd³ assumption throughout.

4. Sustained planning rates for Part 2
Normal: S = R × 0.75 = ______ bags per team-hour
Difficult conditions: S = R × 0.50 = ______ bags per team-hour
Keep rates to one decimal place, or retain calculator precision.

5. What would improve production?
One change and the resource it needs: ____________________
____________________________________________________
Why adding people alone might not help: __________________
____________________________________________________

Data-quality note
Circle: Full trial / Supply-limited / Weather-stopped / Other
If invalid or zero, teacher assigns a labeled practice rate. Do not invent measured results.'''),
('COMMON REFERENCE • STRUCTURE ESTIMATES', '''These are classroom planning assumptions, NOT engineering specifications. Dimensions on scenario cards are proposed planning layouts, not permission to build. Adults and qualified responders approve real work.

Bag geometry model
One flexible filled bag occupies about 1 ft along a line, 0.5 ft across it and 0.25 ft (3 in) in height. The fill conversion remains 75 bags ≈ 1 yd³; geometry is a rough counting model, not a sand-volume measurement.
Single-row line: 1 bag per linear foot per layer.
Narrow line: 1 bag across; two layers = 2 bags per foot.
Broad barrier: triangular cross-section. Three layers have 3 bags across the bottom, 2 in the middle, 1 on top: 6 bags per foot; crest about 9 in. Four layers: 4 + 3 + 2 + 1 = 10 bags per foot; crest about 12 in.
Small erosion-control structure: 2 bags across × 2 layers = 4 bags per foot. These do not support slopes, roads or people.
Basin or low perimeter berm: 2 bags across × 2 layers = 4 bags per foot; crest about 0.5 ft. The oversized basin card explicitly requests 4 across × 4 layers = 16 per foot; crest only 1 ft.
Ground-cover anchor: one bag every 4 ft of perimeter, unless the card supplies a station count. Round bag count up. Approved equipment station: stations × specified bags per station. These are inventory counts, not wind-load ratings.

How to calculate
Straight line: length × bags per foot. Add all separate lines.
U shape: front + two ends; do not count the open side.
L shape: add both legs. Rectangle perimeter = 2 × (length + width).
For basins, use the inside perimeter as a simple estimate; real corner and outer-row adjustments need extra bags. A labeled 10% contingency is acceptable if resources permit.
Round whole bags up. Base fill = bags ÷ 75; report two decimals. Order fill to the next 0.25 yd³, while also checking on-site stock.
Example: a 20 ft broad three-layer line needs 20 × 6 = 120 bags; fill = 120 ÷ 75 = 1.60 yd³; order 1.75 yd³ if buying in quarter yards.

Basin math • planning only
Volume (ft³) = inside length × inside width × water depth.
Gallons ≈ ft³ × 7.48. For water only, approximate load = gallons × 8.3 lb. Do not calculate bag weight.
Use only ground-level, flat, approved sites. Never rooftops, balconies or improvised raised platforms. A two-layer berm has a 0.5 ft theoretical crest; use a proposed operating depth no greater than 0.25 ft unless specifically authorized on the card. Leave freeboard (empty height), plan overflow, prevent access and label NON-POTABLE. Rainfall and liner integrity limit useful supply. This is not drinking or handwashing water.'''),
('COMMON REFERENCE • TIME & SUSTAINMENT', '''Same method for every student
R = your team's completed bags × 3.
Use S = 0.75R for normal planning, including short scenarios. Use S = 0.50R for hot, steep, very muddy or otherwise difficult sustained work; explain your choice. Do not multiply both factors. These factors allow rest, water, role changes and routine delays; they do not replace separate delivery or transport analysis.
N = required bags; T = fully equipped four-person teams.
Experimental team-hours = N ÷ R.
Adjusted team-hours = N ÷ S.
Ideal elapsed production time = N ÷ (T × S).
Deadline minimum teams = round UP [N ÷ (S × usable hours)].
Usable hours = deadline minus initial wait for needed resources and any separate setup allowance. If usable hours ≤ 0, current plan cannot meet the deadline.
Available teams = round DOWN (available workers ÷ 4). Partial groups can support delivery, traffic control or setup, but do not count as another measured team. Only count people actually assigned to the production chain; never assign them two simultaneous jobs.

Elapsed time is more than a division
Your measured rate already included closing, carrying and placing at the experimental route. Compare that distance and equipment with the card. Do not automatically add the same carrying time again. For a changed route, check transport capacity. With separate support workers, stages may overlap: chain rate is limited by the slowest stage. With shared workers, allow a sequential movement period or reduce effective team capacity and explain it. Add delivery waits, setup, inspections and finishing when not included. A capacity estimate is optimistic if people are shared.
A fast estimate: max(adjusted production time, changed-route transport time) + unavoidable initial wait + setup/finish. Use only if the overlapping stages are independently staffed. Otherwise draw a sequential schedule or reserve support workers first. Never double-count a person or cart.

Simplified classroom worker-support rules
Normal: plan 45 min working and 15 min resting/reorganizing each hour; S = 0.75R.
Difficult: plan 30 min working and 30 min resting/reorganizing each hour; S = 0.50R. Shade/cooling/warming breaks as appropriate. Stop if conditions become unsafe; a rate factor does not make unsafe work acceptable.
Drinking-water stock: plan 1 quart per assigned worker per elapsed hour, round up to whole gallons (4 quarts = 1 gallon), plus a 25% reserve rounded up. This is a stock-planning exercise, not a prescribed drinking dose; individuals drink as needed and supervisors adjust for conditions. Refill accessible coolers with safe drinking water.
Food: for more than 4 hours, plan a snack/meal break and one food serving per worker per 4-hour block, rounded up. Keep food away from sand and contamination.
Rotate lifting, shoveling and carrying; put rest areas off routes. Identify a first-aid adult, communication method and relief workers for long operations. Account for support personnel in water and food totals.'''),
('COMMON RESOURCE CATALOG', '''Catalog capacities are classroom assumptions, not vehicle specifications. A card's listed stock is the initial allocation. Catalog entries are things you can request, not free extras. State quantity, arrival time, operator and route.

People & PPE
Worker team: 4 equipped workers. Plan 2 shovels per active team as a starting allocation; fewer requires a rate reduction or measured evidence. More shovels alone do not ensure more throughput.
PPE set: 1 pair work gloves + 1 pair safety glasses per worker; closed-toe shoes required. Cards include one basic set per listed worker unless stated otherwise. Ordinary PPE is not hazardous-material protection.
Sandbags: counted empty bags; no precise bag weights.
Fill: cubic yards; 75 completed bags per yd³. Stock supports about fill × 75 bags.

Movement & deliveries
Wheelbarrow: 4 bags per trip, one operator, 10 min full load/travel/unload/return cycle on a dry level route up to 300 ft one way; 20 min for >300–600 ft. Use fewer bags or a buddy if needed; never force the stated load.
Utility cart: 8 bags per trip, one operator; same cycle times as wheelbarrow. Only approved smooth level routes. Hill, steps or poor ground require a different plan.
Pickup: one qualified adult driver; classroom load 40 bags OR 0.5 yd³ loose fill per trip, never both; 30 min load/travel/unload/return cycle on an approved dry vehicle route. Loading helpers come from the workforce.
Dump truck: supplier driver; 4 yd³ per delivery, 1 h per delivery cycle once service begins. It delivers fill, not finished barriers. Card-specific access and delays override the catalog.
No capacity calculation licenses vehicle overloading; real operators verify ratings. Adult classroom scenarios use these simplified bag counts instead of bag weights.
Trips = round UP (bags ÷ capacity). Transfer time = trips × cycle minutes ÷ 60; divide across identical vehicles only if independently staffed. Loose-fill pickup trips = round UP (yd³ ÷ 0.5).

Other resources you may request
Tarps/plastic sheets and compatible tape: record dimensions and overlaps; check the supplied coverage. Basin liner: base plus berm sides, freeboard and slack; leaks and seams matter. Filter fabric: scenario-specific erosion protection, not structural reinforcement.
Traffic cones and caution tape: mark work zones without blocking exits; never replace proper road closure authority. Rated signs/frames/tents and their required anchors: adult-approved use only.
Flashlights/work lights: request for darkness and verify power/fuel and electrical safety. Radios: plan 1 per team leader plus incident lead if available.
Drinking-water cooler: 5 gal capacity; safe refill source and cups/bottles needed. First-aid kit: at least 1 accessible per work site with trained adult contact.
Basic hand tools: closure supplies, tape measure and approved bag-holding aid; never improvise unsafe shovel stands. Shade/rest space, food, sanitation and waste collection must be arranged.

Card stock default
Unless a card gives a delivery exception, allocated fill has already been delivered to the listed filling point; identify its delivery source and plan any resupply. Every card has basic PPE for its listed workers, one first-aid kit, closure supplies, a tape measure and access to a safe drinking-water refill source. Water containers, food and shade are not automatically supplied: request and schedule them.''')]
worksheet=[('PART 2 • INDIVIDUAL OPERATIONAL PLAN', '''Name: ______________________ Team: ______ Scenario #: ____
Title: __________________________________________________
My observed B: ______  R = 3B: ______ bags/team-hour
Data status: ___________________  S: ______ Factor: 0.75 / 0.50
Why this factor and route comparison? _____________________
____________________________________________________

1. Sketch the proposed layout; label lengths, layers, exits, drainage destination and filling/moving routes. Use the open space below.

[[SKETCH]]


2. Estimate bags and fill
Rule / bags per foot or station: __________________________
Length / perimeter / station calculation: __________________
N = __________________________ bags (round up)
Contingency, if chosen: ______   Revised N: ________________
Fill = N ÷ 75 = ______ yd³; quarter-yard order: ______ yd³
Stock check: bags ______ vs need ______; fill ______ vs need ______
If a basin: ft³ ______; gallons ______; water load ______ lb.
Chosen depth and safe operating limit: ____________________

3. Teams and labor
Available workers: ______; available full teams: ______
Teams actually filling/closing/moving/placing: ______
Support workers (driver/cart/setup/traffic/lead): _____________
Experimental team-hours N ÷ R: _________________________
Adjusted team-hours N ÷ S: _____________________________
Usable hours before deadline: ___________________________
Minimum teams = round up N ÷ (S × usable hours): __________
Compare that minimum with tools/PPE/space available:
____________________________________________________
Ideal production time N ÷ (actual teams × S): ______ hours
Zero rates or no usable time: explain why division fails and state an alternative.

4. Tools, shovels and PPE
Shovels needed: ______; available: ______; response: ________
Other tools / PPE counts / special restrictions:
____________________________________________________
____________________________________________________'''),
('MOVEMENT, TIME & WORKER SUPPORT', '''Name: ______________________ Scenario #: ______

5. Fill delivery and movement
Who delivers fill, how much, where, and when? ______________
____________________________________________________
Filled-bag route and equipment: __________________________
Trips and capacity calculation: ___________________________
Transport time and route limitations: _____________________
How workers are assigned without double-counting: __________
____________________________________________________
Will stages overlap or run in sequence? Why? _______________
____________________________________________________

6. Actual elapsed schedule
Task                         Starts             Ends              People/equipment
Delivery/setup: ________________________________________
Filling/closing: _________________________________________
Movement/placing: ______________________________________
Rest/rotation/finish/check: _______________________________
Expected completion: ______ hours after start
Deadline: ______ hours; margin/shortfall: ___________________
If route differs from experiment, how is time corrected? ______
____________________________________________________

7. Water, food, rest and first aid
Water gallons = workers × elapsed hours ÷ 4: _______________
Rounded base stock: ______; plus 25% reserve: ______ gal total
5 gal coolers needed / refill schedule: _____________________
Safe water delivery and accessible location: _________________
Food needed? Why? _____________________________________
Servings and meal-break timing: __________________________
Rest/rotation pattern and relief assignments: _________________
Shade/weather protection and first-aid adult: _________________

8. Other materials and limiting resource
Material                           Quantity/dimensions            Arrival/source
____________________________________________________
____________________________________________________
____________________________________________________
Most likely bottleneck; evidence and fix: ____________________
____________________________________________________
____________________________________________________
Name an additional constraint that could replace this bottleneck:
____________________________________________________'''),
('DECISION, INCIDENT REVISION & AFTER-ACTION REVIEW', '''Name: ______________________ Scenario #: ______

9. Is this practical?
Circle: Proceed as proposed / Proceed with changes / Reject primary bag plan
Explain using resources, time, safe site conditions and the mission:
____________________________________________________
____________________________________________________
What should emergency managers change? _________________
____________________________________________________
What will you protect first, and what may remain unprotected?
____________________________________________________
Stop/relocate trigger and who makes the decision: ____________
____________________________________________________

10. Incident update
Card #: ______ Update: __________________________________
Which assumptions or resources changed? ___________________
____________________________________________________
New bag/fill/team/transport/time/support estimates as needed:
____________________________________________________
____________________________________________________
Revised priorities and request to incident lead: _______________
____________________________________________________
Revised expected completion / deadline result: _______________
____________________________________________________
What uncertainty remains? ________________________________

11. Short after-action review
Which part of your initial plan failed first? ___________________
____________________________________________________
Which physical-trial observation helped your plan most? _______
____________________________________________________
Why isn't 'we need 600 sandbags' an operational plan?
____________________________________________________
____________________________________________________
One change you would make in a second 20-minute trial:
____________________________________________________

Optional extensions
Compare a shorter targeted barrier with moving equipment. Calculate how much one extra cart helps and when shovels become limiting. Test a 10% bag contingency. Design a fair second trial changing only one variable. Explain why two teams with the same bag count can finish a mission at different times.''')]
updates=[
('Delivery slips','The first needed sand delivery will arrive 90 minutes later than your plan. Rebuild your schedule, choose work possible before delivery, and decide whether the priority needs to change.'),
('Truck access denied','The truck cannot reach your filling site. Its nearest approved drop is 600 ft away on a dry level route. Plan fill transfer or move filling; account for people and equipment.'),
('Last 300 feet on foot','Vehicle access ends 300 ft before the final position. Only wheelbarrows fit beyond that point. Recalculate trips and assign operators without double-counting.'),
('Workers leave','Four listed workers become unavailable immediately. If your card has only four, no production team remains. Revise priorities, request help or suspend deployment.'),
('Equipped volunteers','Eight trained adult volunteers arrive in one hour with basic PPE but no tools. Determine what useful jobs they can do and what additional resources actually improve throughput.'),
('Volunteers without PPE','Eight volunteers arrive now with no gloves or safety glasses. Do not count them in production until equipped. Assign safe support work or request PPE and give an arrival time.'),
('Broken shovels','Two shovels fail; if fewer than two were available, all fail. Reorganize work and show how the new tool bottleneck changes the plan.'),
('Hotter conditions','Temperature rises to 90°F with humid conditions. Use the difficult factor instead of the normal factor for remaining production. Revise rest, shade and water supply; consider suspension.'),
('Rain arrives early','Heavy rain starts one hour earlier than forecast. Shorten the deadline by one hour; if no time remains, state a safe fallback. Do not continue into moving water.'),
('Darkness','Daylight ends in 45 minutes. You have no powered work lights allocated. Request lighting and power with an arrival time, shorten the mission, or stop safely.'),
('Accessible doorway','A 6 ft accessible doorway must stay open through your proposed layout. Redraw a safe diversion route and re-estimate materials; do not simply omit bags and claim equal protection.'),
('Vehicle route','A 14 ft emergency vehicle lane must remain clear. Change placement, stockpiles and transport routes; identify who controls access.'),
('Short sand supply','Only 75% of the planned fill arrives. Calculate supported bags, choose a reduced mission and explain what cannot be protected.'),
('Second priority','An occupied shelter now needs a 20 ft narrow two-layer diversion line 400 ft from your site. Share the current resources and explain which mission takes priority.'),
('Wheelbarrow loss','One wheelbarrow is unavailable; if none was listed, the utility cart becomes unavailable instead. If neither exists, the approved pickup route closes. Develop a different movement plan.'),
('Water shortage','Only half your planned drinking-water stock is available. Arrange safe resupply, reduce staffing duration or suspend physical work; changing math alone does not supply water.'),
('Public works delay','Public Works offers one additional cart and two shovels, but they arrive in two hours. Compare a wait-and-work plan with immediate reduced deployment.'),
('Priority changes','Emergency management now prioritizes people and accessible exits over property protection. State which parts of your mission remain useful and redirect resources.'),
('Drainage destination fails','Your receiving drain, swale or overflow area is unavailable. For an infrastructure card, its approved placement route is unavailable. Obtain a new approved location before claiming a workable plan.'),
('Request exceeds stock','Command asks you to double the proposed structure with no new stock or deadline extension. Estimate the gap and offer a feasible reduced alternative.'),
('PPE inventory error','Four basic PPE sets were counted twice. Recalculate the equipped workforce; request replacements and plan safe work until they arrive.'),
('Route slows down','The approved movement route becomes slower but remains safe. Double cart/wheelbarrow cycle time; if carrying by hand, use the difficult factor for remaining work. Rebuild the staffing and schedule.'),
('Better alternative arrives','In one hour a qualified crew can provide an approved alternative: drainage repair for water scenarios, containers for basins, rated anchors for infrastructure, or stabilization/containment equipment for other cases. Compare partial bagging with changing the mission.'),
('Stop for lightning','Thunder is heard. All outdoor work stops and workers shelter indoors. Teacher supplies a 45-minute lost-time allowance for classroom calculations; actual restart follows school weather policy. Revise schedule and decision.')]
teacher=[('TEACHER GUIDE • PURPOSE & PACKAGE', '''Sandbag Emergency Logistics • Zombie Invasion Prep
Central lesson: Emergency response is a logistics problem.
Bags → fill → transportation → people → equipment → time → sustainment.
Having a resource is different from being able to employ it. A strong plan meets the mission with available resources, recognizes bottlenecks, and changes when conditions change.

Print and distribute
Part 1: pages 1–2 per four-person team; reference pages 3–5 per student. Part 2 planning worksheet: three pages per student. Scenario bank: one different one-page card per student; 30 available. Updates: cut the six four-card pages into 24 reusable cards. Teacher guide is separate; do not distribute its estimates before planning.
Editable Markdown files accompany every PDF, plus a complete editable package and the generation script/data. Print US Letter at actual size; grayscale-friendly design. No weights or online research are needed from students.

Suggested sequence
Session 1: 10–15 min briefing and demonstration, 20 min field trial, 10 min cleanup/count/calculations, 10 min comparison. Reserve additional time for setup, handwashing and travel outside.
Session 2: review common rules (10 min), assign individual cards and plan (30–40 min), introduce one update and revise (10–15 min), debrief (10 min). Use a third session for presentation or extensions if needed.
Teams share their experimental rate, but each student owns a different emergency plan. Distribute cards randomly or by challenge; scenarios 11, 12, 15, 19, 27 and 30 deliberately demand redesign or rejection. No neighborhood or street knowledge is required. All situations are fictional regional composites.

Objectives and evidence
Students measure an actual production chain, calculate rates/fill/team-hours, distinguish ideal and elapsed time, allocate workers and tools, and support workers. Evidence includes field data, labeled sketch, calculations, schedule, resource requests, decision and revised plan. Do not award the highest score merely for the greatest bag count or the largest barrier.

Availability of roughly 50 physical bags
With 30 students you may have seven full teams plus two support observers. Fifty bags total may limit a simultaneous trial. Obtain extra bags when possible, or run staggered trials using the same bags only between trials (teacher-approved emptying/reset). Allocate enough bags that a team is unlikely to run out; monitor and replenish before a queue forms. Record supply-limited trials explicitly. Do not interpret a team cap as its physical maximum.'''),
('TEACHER GUIDE • FIELD PROTOCOL & SAFETY', '''Before students arrive
Inspect a dry, level practice area away from roads, drains and unstable slopes. Use clean sand, flexible bags, appropriately sized shovels, gloves, safety glasses and closed-toe footwear. Mark a short carry route, fill zones and a destination large enough for neat placement. Provide safe drinking water, rest space, a first-aid adult and handwashing. Verify school supervision and weather procedures. Offer meaningful non-lifting roles and accessible alternatives.

Standardize the experiment
Make a sample bag half to two-thirds full and comfortably manageable. This is a visual/tactile standard, not a weighed target. Underfill for safe handling when needed, but note differing standards when comparing teams. Demonstrate consistent closure: fold/tuck or teacher-approved tie. Do not require students to tie densely packed bags. Teach safe shoveling, controlled lifting/placement and buddy handling; no throwing or running. A teacher inspection determines acceptable completion.
Keep four workers, 20 minutes, route distance, fill standard and count definition consistent when possible. Record every equipment difference. Supply gloves and glasses for everyone. Bags counted must be filled, closed, moved and placed at the designated endpoint. Do not count work in progress when the timer ends.

Run the trial
Allow teams to choose roles. Start the clock together; observe queues and role changes. Permit rest and safety stops without penalty. Stop immediately for lightning/thunder, unsafe weather, pain, fatigue or any hazardous condition. Follow school restart policy; never turn a weather stop into a speed challenge. At 20 min, stop all production and count accepted bags once. Record early material exhaustion, elapsed time and route conditions.
A teacher may run another supplied trial later, or assign a clearly labeled classroom practice rate if the result is zero/invalid. Example practice rate: B = 20; R = 60. Do not replace genuine observations without labeling them. Do not normalize a capped count as though it measured unconstrained capacity.

Cleanup
Adults control any emptying/reset. Avoid airborne dust; return sand to the designated pile, store bags dry, inspect tools, account for students and wash hands before food. No student-built emergency structure is tested with floodwater.

Planning-scenario boundaries
All field production is on the safe practice site. Cards about floods, electrical equipment, contaminants, slopes or emergency vehicles are paper exercises for adult response planning. Gloves/glasses do not authorize hazardous work. Bags are not watertight, a flood guarantee, a retaining wall or a tent wind rating. Do not imply that a class estimate is a real construction specification. Real deployment needs agency approval, site assessment, proper materials and safe withdrawal decisions.'''),
('TEACHER GUIDE • CALCULATION & ASSESSMENT', '''Use each student's measured R; there is no universal completion time.
Baseline estimates on following pages have no contingency. Accept a reasoned 10% extra or alternative safe layout; require the student to check its resource impact. Basin estimates omit outer-row/corner adjustments deliberately. Every card gives sufficient dimensions for the shared counting rules.

Worked method, not a fixed answer key
If B = 20 bags, R = 60 bags/team-hour. Normal S = 45; difficult S = 30. A 120-bag mission needs 2 experimental team-hours or 2.67 adjusted team-hours at normal conditions. Two fully equipped production teams would take at least 1.33 h. That is not a guaranteed finish: staffing transport separately, delivery, route, setup and inspection can increase elapsed time.
The catalog's starting point is two shovels per team. With only two shovels for three teams, accept using one production team plus helpers, requesting tools, or a clearly justified lower rate. Never credit three full-rate teams solely because 12 people are present. Supplementary drivers/operators must be counted. A two-worker support group cannot be treated as a measured four-worker team.
At 1 wheelbarrow, 4 bags/10 min gives a catalog upper bound of 24 bags/h; 1 cart gives 48 bags/h. On 301–600 ft routes these fall to 12 and 24 bags/h. These are movement-only ceilings with an operator, not added guaranteed production. Pickups move at most 80 bags/h under the supplied cycle. Shared loading labor reduces production capacity. On steep routes catalog cycles are optimistic; seek a new route or lower capacity rather than treating 0.50 as a precise transport model.
Do not add normal trial carrying time again. On changed routes, compare the chain's limiting rate and show a staffing/schedule method. Minimum deadline teams is an ideal lower bound, not a promise of feasibility. Give credit for identifying unquantified setup and adding a labeled allowance (e.g., 15–30 min); don't demand a hidden standard.

Sustainment example
Eight workers for 3 elapsed hours: 8 × 3 ÷ 4 = 6 gal base; with 25% reserve, round up 7.5 to 8 gal. Two 5 gal coolers, with accessible refill, provide adequate capacity. Count support staff too. More than 4 h: food servings = workers × round up(elapsed hours ÷ 4); normal breaks remain in the 0.75 rate and should not be added a second time unless extra meal breaks are chosen.

Suggested assessment • 20 points
Field evidence and honest rate labeling: 3. Sketch/bag/fill reasoning: 4. People/tools/movement/schedule feasibility: 5. Sustainment/safety/materials: 3. Practical decision and alternatives: 3. Incident revision with changed priorities/resources: 2.
Accept justified ranges and uncertainty. Major omissions include treating empty bags as completed protection, ignoring sand delivery, double-counting workers, claiming unlimited scaling, ignoring access, or continuing a fundamentally unsafe mission. A well-supported rejection can earn full credit.''')]
for s in sc:
 n=s['n']; f=n/75; t=s['workers']//4; a=n/(t*.75); b=n/(t*.5)
 support=[]
 if s['bags']<n: support.append(f"Empty bags short by {n-s['bags']}.")
 initial_fill = 6 if s['id']==29 else s['fill']
 if initial_fill<f: support.append(f"Initial fill short by {f-initial_fill:.2f} yd³; confirm delivery before claiming production.")
 if s['shovels']<2*t: support.append(f"{s['shovels']} shovels versus starting allocation {2*t}; tool-limited full-rate teams ≤ {s['shovels']//2} without evidence of another method.")
 if s['id']==29: support.append('Total allocated fill is 10 yd³: 6 initially + 4 after 2 h, although the supplier allocation is 12 yd³. Base need is 9.60; additional reserve would need another delivery.')
 basin=''
 if s['id'] in [18,19,20]:
  l,w,d={18:(12,8,.5),19:(30,20,2),20:(10,10,.25)}[s['id']]; v=l*w*d; g=v*7.48
  basin=f"\nBasin: requested {v:.0f} ft³ = {g:.2f} gal ≈ {g*8.3:,.0f} lb of water. "
  if s['id']==18: basin+='Authorized 0.5 ft depth leaves no modeled freeboard; prefer 0.25 ft (24 ft³; 179.52 gal; about 1,490 lb) with approved liner and overflow. Authorization is not a safety guarantee.'
  if s['id']==19: basin+='Requested depth is twice the modeled crest; not feasible. Even a shallower design requires ground/site approval and a much larger liner. Approved containers or delivery are preferable.'
  if s['id']==20: basin+='0.25 ft leaves 0.25 ft modeled freeboard. Check flat ground, liner, overflow, access control and allowed non-potable use.'
 calculation={1:'24 × 2',2:'36 × 6',3:'(18 + 18) × 2',4:'(16 + 8 + 8) × 2',5:'(12 + 8) × 2',6:'48 × 2',7:'60 × 2',8:'30 × 2',9:'(10 + 8 + 8) × 2',10:'3 × (4 + 2 + 2) × 6',11:'480 × 6',12:'120 × 10',13:'3 × 8 × 4',14:'30 × 4',15:'4 × 25 × 4',16:'2 × 15 × 4',17:'3 × 12 × 4',18:'2 × (12 + 8) × 4',19:'2 × (30 + 20) × 16',20:'2 × (10 + 10) × 4',21:'2 × (20 + 12) ÷ 4',22:'6 × 2',23:'8 × 4',24:'10 × 2',25:'2 × (40 + 20) ÷ 4',26:'50 × 3',27:'80 × 6',28:'90 × 2',29:'120 × 6',30:'30 × 2 + 60 × 6'}[s['id']]
 teacher.append((f"ESTIMATE GUIDE {s['id']:02d} • {s['title']}",f'''Baseline structure estimate
{calculation} = {n:,} bags. A labeled 10% contingency would be {math.ceil(n*1.1):,} bags; check revised fill and supply. Alternative approved shorter layouts may be reasonable if the mission changes explicitly.
Base fill: {n} ÷ 75 = {f:.2f} yd³. Quarter-yard order: {math.ceil(f*4)/4:.2f} yd³.

Labor using the student's own R
Experimental team-hours = {n}/R.
Normal adjusted team-hours = {n}/(0.75R); difficult = {n}/(0.50R).
Listed workers {s['workers']} = at most {t} full teams BEFORE support/tool deductions.
Ideal elapsed lower bound if every listed team is equipped and dedicated: normal {a:.2f}/R h; difficult {b:.2f}/R h. Substitute the actual measured R. Do not use these coefficients as hours by themselves.
Deadline lower bound: round up [{n} ÷ (S × usable hours)]; card deadline {s['deadline']:g} h. Initial unavoidable wait: {s['arrival']:g} h. Subtract additional setup as justified.

Stock and staffing checks
{' '.join(support) if support else 'Base bag/fill allocation covers the requested structure, but movement, staffing and elapsed time still require checks.'}
Basic PPE for {s['workers']} people is supplied; assign the two-shovels-per-team starting allocation, safe fill workspace and operators. Calculate water, coolers, food, rest and relief from the final elapsed schedule, not merely the nominal deadline.

Major constraint / likely bottleneck
{s['constraint']} Equipment: {s['equipment']}. Compare its movement capacity with production at the measured distance. Delivery, route, stock or tools may become the limiting stage. The fastest plausible arithmetic is not necessarily feasible.

Practicality and strong-response considerations
{s['reason']}
Additional materials/arrangements: {s['extra']}.
Strong responses verify where water will go, preserve access, identify stop/relocate conditions, distinguish safe partial work from complete mission success, and name resource requests with arrival times. For infrastructure, require rated equipment/adult approval rather than inventing ballast ratings. For hazardous runoff, ordinary PPE never authorizes entry.
{basin}'''))
teacher += [('TEACHER GUIDE • INCIDENTS & DEBRIEF', '''Introduce updates after initial plans are complete
Give each student one update, or give the whole class the same one to compare decisions. Read card changes as modifications to their scenario; all other resources remain as stated. Ask students to mark what changes in their sketch, staffing, schedule, supply requests, worker support and priority decision. If an update is irrelevant to a particular structure, use its stated infrastructure adaptation or select another card.
For mid-operation updates, specify time elapsed and completed bags before recalculation. Example: issue the card before work begins, or say “one hour has elapsed and 30 bags are already placed.” Apply factors only to remaining bags; count completed bags once. Do not award credit for a multiplication alone without a revised operational decision.

Teacher revision checks
Delivery delay: shift the critical start or split tasks; no fictitious early fill. Extra volunteers: PPE, shovels, transport and workspace still constrain production. Failed tools/cart: reorganize the chain and staffing. Heat: replace factor, not multiply both, and revise water/rest. Unsafe weather: stop and shelter. New access/drainage restriction: redraw rather than claim an incomplete barrier gives equal protection. Added mission/short supply: prioritize people and essential services, identify residual risk, request alternatives. An impossible request needs an explicit refusal or reduced mission.

Debrief prompts • 10 minutes
What was your measured bottleneck? Did it remain the bottleneck on the new site? Which resource existed but could not be employed? How did a longer route change the apparent production rate? What did a water/rest plan change? Which rejected bag plan was the strongest decision? What uncertainty would you check first as the incident lead?
Have each student finish: “Our plan needs ___, delivered by ___, at ___, with ___ people, and will finish by ___ unless ___.”

Optional extensions
Compare two safe carry distances in controlled trials, changing one variable. Use a chart of output versus time to show why a 20-minute rate is not an all-day promise. Allocate a shared truck across three sites with different deadlines. Add 10% bag reserve and recalculate ordered fill. Determine how many extra shovels/carts change the actual bottleneck. Compare basin gallons with approved container delivery, including cleanup and water availability. Estimate uncertainty ranges instead of inventing precise engineering strength.'''),
('TEACHER BACKGROUND • SOURCES & LIMITS', '''Sources checked for this package
U.S. Army Corps of Engineers, Jacksonville District, Sandbag Information:
https://www.saj.usace.army.mil/Missions/Emergency-Operations/Sandbag-information/
Background for partial filling, gloves, staggered placement and plastic use. The classroom trial's consistent closure/counting standard is an instructional choice.
U.S. Army Corps of Engineers, Rock Island District, NFFMC Supplies:
https://www.mvr.usace.army.mil/missions/emergency-management/nffmc/supplies/
Background for temporary barriers, sheet ballast and plastic sheeting; not validation of the classroom count geometry.
National Weather Service, Flood Watch vs. Warning:
https://www.weather.gov/safety/flood-watch-warning
Background for imminent flood hazards and avoiding flooded roads. Check official local forecasts and school procedures on the day of the actual outdoor lesson.
National Weather Service Pittsburgh:
https://www.weather.gov/pbz/
Local weather information; scenarios are fictional, not current forecasts or site assessments.

Authorship of simplified assumptions
The universal 75 bags ≈ 1 yd³ conversion comes from the course brief and is used consistently. One-foot bag length, three-inch modeled layers, structural bag counts, catalog trip capacities/cycles, 0.75/0.50 rate factors, water stock and food intervals are supplied classroom assumptions. They are not quoted agency design standards or medically prescribed doses. Water conversion: 1 ft³ ≈ 7.48 gallons; approximate water load uses 8.3 lb per gallon. Do not extend water-load math to bag weighing.

Limits to make explicit
A filled bag must be moved and positioned to become useful. Barriers leak; drainage destinations and neighbors matter. Simplified structures do not establish a safe flood height, slope strength, retaining capacity, containment compatibility or equipment anchorage. Deep or moving floodwater, unstable ground, electricity and hazardous materials require qualified response and may require withdrawal. Students plan on paper; their field task remains the safe, supervised production experiment.''')]
# Specific logistics notes supplement the shared estimate method.
logistics = {
1: 'One wheelbarrow needs 12 trips, 2.00 h movement-only. Hand carrying on the short route may be better; compare with the measured trial.',
2: 'Two wheelbarrows: 54 total trips, 27 cycles each, 4.50 h movement-only, exceeding the 4 h deadline before setup. Add transport, carry by an evidenced faster method, or shorten the line.',
3: 'One cart: 9 trips, 1.50 h movement-only. Two shovels serve only one normal full-rate filling team; roles and cart staffing must be justified.',
4: 'One wheelbarrow: 16 trips, 2.67 h movement-only versus a 2 h deadline. A shorter targeted line, additional transport or relocating the trailer deserves consideration.',
5: 'Only one team and 45 min. Hand carrying cannot be priced from the cart catalog; compare with the trial and reserve time for utility clearance. Moving vulnerable contents may be faster.',
6: 'Two carts: 12 total trips, 6 cycles each, 1.00 h movement-only. This excludes production; four shovels and emergency vehicle access limit scaling.',
7: 'One wheelbarrow: 30 trips, 5.00 h movement-only versus 4 h. Shovels and movement both limit the 12-person workforce; request a cart or reduce scope.',
8: 'One cart: 8 trips, 1.33 h movement-only versus 1.5 h. Utility shutoff/source control may finish sooner and should lead the response.',
9: 'One wheelbarrow: 13 trips, 2.17 h movement-only versus 2 h. Heat calls for difficult-rate reasoning; safely moving the generator may be preferable.',
10: 'One cart: 18 trips, 3.00 h movement-only, using the entire deadline. A short hand route, parallel carrying or a smaller targeted approach needs evidence.',
11: 'Even all 400 bags form only about 66 ft of broad three-layer line; complete 480 ft protection is unsupported. Relocation is the likely priority.',
12: 'Bag shortage is 400, but fixing it would not make the proposal safe. The road must close and responders use a dry detour.',
13: 'One wheelbarrow: 24 trips, 4.00 h movement-only, leaving no production/setup margin. Target the highest-priority approved structure or request transport.',
14: 'Two wheelbarrows: 30 total trips, 15 cycles each, 2.50 h movement-only. Deadline margin is small; preserve closure and inspect permanent repair needs.',
15: 'The proposed bag count is not a slope-stability calculation. Do not dispatch the one wheelbarrow or workers into the exclusion zone.',
16: 'One wheelbarrow: 30 trips, 5.00 h movement-only versus 4 h. Reduce to an approved priority segment or wait for the repair crew while retaining closure.',
17: 'One wheelbarrow: 36 trips, 6.00 h movement-only versus 4 h. The lone team cannot also supply independent transport staffing at a full team rate.',
18: 'One cart: 20 trips, 3.33 h movement-only versus 4 h. No guaranteed rainfall; liner setup and basin supervision add time and responsibilities.',
19: 'Even 500 bags provide only 31.25 ft at 16 bags/ft, against a 100 ft perimeter. Bagging cannot fix insufficient crest, liner or unsafe water load.',
20: 'One wheelbarrow: 40 trips, 6.67 h movement-only versus 3 h. Approved delivered containers or a smaller supervised reserve are more plausible.',
21: 'One cart: 2 trips, 0.33 h movement-only. Sixteen bags use 0.21 yd³, so ordering a full truckload would be disproportionate.',
22: 'One cart: 2 trips, 0.33 h movement-only. Rated frame placement, egress and inspection may take longer than filling the 12 bags.',
23: 'One cart: 4 trips, 0.67 h movement-only. The bag inventory cannot establish tent safety in thunderstorms; verify anchors and indoor shelter.',
24: 'One cart: 3 trips, 0.50 h minimum movement-only on routes up to 300 ft from the midpoint. Distributed stops and sign checks add time.',
25: 'One wheelbarrow: 8 trips, 1.33 h movement-only. Control tarp edges and wind exposure; a tarp is not a debris-containment design.',
26: 'One wheelbarrow: 38 trips, 6.33 h movement-only versus 1 h. No ordinary team deployment is authorized into contamination; professional source control/containment is urgent.',
27: 'Short 180 bags and 2.40 yd³ fill. Two wheelbarrows would need 60 cycles per operator, 10 h movement-only. Isolation and professional recovery are preferable to this deadline claim.',
28: '180 bags need 2.40 yd³. A pickup transferring loose fill needs 5 trips (2.50 h) after the 1 h delivery delay, before a final safe uphill movement stage. Filling at alternate staging could trade fill transfer for bag movement, but pickup access and the uphill last mile still govern.',
29: '720 bags need 9.60 yd³. Two wheelbarrows alone require 15 h movement-only, so the approved pickup route or a shorter staging route matters. Pickup alone needs 18 cycles (9 h); assign driver/loading help and staged delivery. A 10% bag reserve raises fill to 10.56 yd³, requiring another delivery beyond the first 10 yd³ on site.',
30: 'Shelter needs 60 bags and 0.80 yd³; recreation site 360 bags and 4.80 yd³. Total 420 bags and 5.60 yd³ exceeds stock by 70 bags and 0.60 yd³. Shelter cart movement is 8 trips (1.33 h), longer than its 1 h deadline unless an evidenced faster safe method is used. Prioritize shelter and request help rather than promise both.'
}
for idx,entry in enumerate(teacher):
 title,body=entry
 if title.startswith('ESTIMATE GUIDE '):
  num=int(title.split()[2])
  teacher[idx]=(title,body.replace('\nPracticality and strong-response considerations','\nSpecific logistics check\n'+logistics[num]+'\n\nPracticality and strong-response considerations'))
# PDF renderer: each tuple is an intentional page; Markdown remains editable.
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyClean',fontName='Helvetica',fontSize=10,leading=13,spaceAfter=5,textColor=colors.HexColor('#202a32')))
styles.add(ParagraphStyle(name='PageTitle',fontName='Helvetica-Bold',fontSize=17,leading=20,spaceAfter=12,textColor=colors.HexColor('#163d4b')))
styles.add(ParagraphStyle(name='SectionClean',fontName='Helvetica-Bold',fontSize=10.5,leading=14,spaceBefore=6,spaceAfter=4,textColor=colors.HexColor('#163d4b')))
styles.add(ParagraphStyle(name='CardText',fontName='Helvetica',fontSize=10,leading=13,spaceAfter=6))
# Render plain-text paragraphs without using raw Markdown as PDF layout.
def blocks(body):
 result=[]
 for group in body.strip().split('\n\n'):
  if group.strip()=='[[SKETCH]]':
   result.append(Spacer(1,80)); continue
  if not group.strip(): continue
  lines=group.split('\n')
  if len(lines)>1 and len(lines[0])<90 and not lines[0].startswith(('http','Name:','Date:','Four team','Workers:')):
   result.append(Paragraph(html.escape(lines[0]),styles['SectionClean']))
   txt='\n'.join(lines[1:])
  else: txt=group
  result.append(Paragraph(html.escape(txt).replace('\n','<br/>'),styles['BodyClean']))
 return result

def footer(canvas,doc):
 canvas.saveState(); canvas.setStrokeColor(colors.HexColor('#a8b4ba')); canvas.line(42,35,570,35)
 canvas.setFont('Helvetica',8); canvas.setFillColor(colors.HexColor('#4b5961'))
 canvas.drawString(42,23,'ZOMBIE INVASION PREP  |  Sandbag Emergency Logistics')
 canvas.drawRightString(570,23,str(doc.page)); canvas.restoreState()

def request_footer(canvas,doc):
 footer(canvas,doc)
 canvas.saveState()
 canvas.setStrokeColor(colors.HexColor('#163d4b'))
 canvas.setLineWidth(1.2)
 canvas.line(42,769,570,769)
 canvas.setFont('Helvetica-Bold',7)
 canvas.setFillColor(colors.HexColor('#26343b'))
 canvas.drawString(42,775,'ZIP / EMERGENCY LOGISTICS')
 canvas.drawRightString(570,775,f'OPERATIONS REQUEST {doc.page:02d}  •  TRAINING')
 canvas.restoreState()

def write(name,pages):
 md='\n\n---\n\n'.join('# '+title+'\n\n'+body for title,body in pages)+'\n'
 (OUT/(name+'.md')).write_text(md)
 story=[]
 for i,(title,body) in enumerate(pages):
  if i: story.append(PageBreak())
  story.append(Paragraph(html.escape(title),styles['PageTitle']))
  story+=blocks(body)
 doc=SimpleDocTemplate(str(OUT/(name+'.pdf')),pagesize=letter,rightMargin=42,leftMargin=42,topMargin=40,bottomMargin=48,title=name.replace('-',' '),author='Zombie Invasion Prep')
 page_callback=request_footer if name=='03-student-scenario-bank' else footer
 doc.build(story,onFirstPage=page_callback,onLaterPages=page_callback)

# Revision: mission-based requests; students choose resources, structure and staffing.
revisions = [
('Keep shallow runoff away from the library entrance until the storm passes.','Runoff crosses a 24 ft frontage. A safe grass swale is available downhill; a possible fill staging area is 40 ft away.','A 6 ft accessible entrance must remain open; do not send water toward neighboring property.'),
('Protect the exposed side of the community center from a forecast shallow creek rise.','36 ft exposed frontage; water may reach 6 in depth. A possible filling area is 120 ft away.','Protect the occupied building while preserving exits and a way for rainwater behind the barrier to drain.'),
('Keep the school shelter entrance usable during the storm.','An 18 ft-long, 6 ft-wide walkway has runoff entering from both edges. A possible filling area is 60 ft away.','Wheelchairs, families and emergency staff need continuous access.'),
('Keep shallow surface runoff away from the communications trailer, or recommend a better location.','Trailer footprint 16 × 8 ft; runoff approaches its uphill long side and both ends. A potential filling area is 100 ft away.','Communications must stay operational. Vents, cables, access and a safe drainage outlet must remain clear.'),
('Reduce shallow runoff approaching the utility cabinet while utility staff respond.','Exposed sides are 12 ft and 8 ft long. A possible fill site is 80 ft away.','Utility staff control the exclusion zone and all electrical work. Work must stop if the dry area becomes unsafe.'),
('Keep runoff out of the fire station bays and keep emergency vehicles moving.','A damaged drain affects a 48 ft stretch of apron. A second inlet may be usable after Public Works approval; fill staging is 180 ft away.','A 14 ft vehicle exit must remain open. Do not block drainage openings.'),
('Keep schoolyard runoff away from occupied areas until the collapsed inlet is repaired.','Runoff affects a 60 ft stretch. A grass drainage channel may accept diversion after approval; staging is 200 ft away.','The school stays occupied. Keep work zones separated from children and verify the receiving drainage capacity.'),
('Protect the EMS supply-room entrance until utility crews shut off the broken main.','30 ft of approach is exposed to shallow water; a possible fill area is 90 ft away.','Avoid undermined pavement. Compare temporary bagging with source control and relocating supplies.'),
('Keep an emergency-site generator operating safely through shallow hillside runoff.','Generator pad 10 × 8 ft; water approaches the uphill side and both ends. A potential fill area is 150 ft away.','The operator must retain fueling access, ventilation and electrical clearances. Relocation may be necessary.'),
('Reduce runoff entering three community-building basement window wells.','Each well has a 4 ft front and two 2 ft sides. A possible fill area is 50 ft away.','Keep emergency exits and ventilation usable; surface protection does not eliminate basement seepage.'),
('Assess protection of the riverfront storage frontage and recommend an achievable response.','480 ft exposed frontage; forecast water depth 6 in. Possible fill staging is 300 ft away.','Critical inventory can instead be relocated by adult crews. Compare bagging the whole frontage with targeted protection or relocation.'),
('Assess whether sandbags can keep the road usable; recommend a safe emergency-access plan.','120 ft road crossing; forecast moving water depth 18 in. Possible fill staging is 100 ft away.','A dry detour exists. Nobody enters moving floodwater; the classroom barrier model is not a roadway flood defense design.'),
('Reduce additional runoff damage above a washed-out trail until the repair crew arrives.','Three damaged areas, each about 8 ft across; possible fill staging 160 ft away.','The trail remains closed. The proposed treatment cannot serve as a replacement walking surface.'),
('Limit further surface erosion near a closed road shoulder pending inspection.','30 ft of affected shoulder; possible fill staging 250 ft away.','Bags cannot support traffic or justify reopening the road. Public Works must approve any temporary treatment.'),
('Assess a resident request to use sandbags to hold a cracked hillside in place.','Four affected slope sections, each 25 ft across; dry staging 200 ft outside the exclusion zone.','No entry into the slide zone. Distinguish surface runoff control from actual slope stabilization.'),
('Reduce additional erosion at the culvert approach while awaiting permanent repair.','Two affected areas, each 15 ft across; possible fill staging 220 ft away.','Keep the culvert opening clear and the approach closed. Avoid backing water upstream.'),
('Assess temporary protection of three scour areas beside a closed ballfield.','Three affected areas, each 12 ft across; dry fill staging 280 ft away.','No work in the creek or at the unstable bank edge. A professional crew must handle permanent stabilization.'),
('Assess a temporary lined collection basin for adult-managed cleaning water.','Suggested inside footprint 12 × 8 ft on flat ground; requested depth up to 0.5 ft; possible fill staging 80 ft away.','Water is NON-POTABLE. Set a sensible operating depth with freeboard and overflow; rainfall supply is uncertain.'),
('Evaluate the requested rainwater basin and recommend a workable storage plan.','Requested inside footprint 30 × 20 ft and water depth 2 ft; ground-level paved site; possible fill staging 300 ft away.','There is no approved deep-basin design. Calculate the water load and compare smaller basins or approved containers.'),
('Assess a small adult-managed non-potable water reserve for a temporary clinic.','Suggested inside footprint 10 × 10 ft and depth 0.25 ft; fill staging 300 ft away via a dry level pedestrian route.','No vehicle fits the last 300 ft. Water is not for drinking or handwashing; compare collection with delivered containers.'),
('Hold a ground-cover tarp in place for a dry shelter staging area.','Ground-cover footprint 20 × 12 ft; potential fill staging 60 ft away.','This is ground cover, not an overhead shelter. Keep edges out of accessible walking routes.'),
('Plan supplementary ballast for approved shelter privacy-screen frames.','Six approved base stations; supervisor requests two bags per station. Possible fill staging 80 ft from the entrance.','Only the rated frame system may be used; keep exits open and protect the floor.'),
('Plan supplementary ballast for an approved mobile charging tent.','Eight approved ballast stations; site supervisor requests four bags per station. Potential fill staging 150 ft away.','The manufacturer still controls anchoring. Sandbag quantities do not establish a wind rating; plan indoor shelter for thunderstorms.'),
('Place temporary wayfinding signs throughout an emergency assistance site.','Ten approved stands; supervisor requests two bags per stand. Signs extend along a 600 ft pedestrian route; possible fill staging at the midpoint.','The route stays accessible. Allow time for distributed placement and checking visibility.'),
('Hold down a debris-sorting ground tarp before Public Works begins sorting.','Ground tarp footprint 40 × 20 ft; possible fill staging 200 ft away.','Adult crews inspect debris and the site. Tarp ballast is not hazardous-material containment.'),
('Assess temporary protection of a storm inlet from potentially contaminated runoff.','50 ft threatened boundary; potential clean-zone fill staging 100 ft away.','Planning only: hazardous-material responders authorize all work, containment destinations and PPE. Students never handle contamination.'),
('Assess clean-side protection around a flooded maintenance yard.','80 ft affected boundary; possible clean staging 250 ft away.','Water may contain oil or other contaminants. Trained responders control entry, compatible materials, recovery and disposal.'),
('Keep hillside school runoff away from occupied areas despite difficult delivery access.','90 ft affected frontage; nearest approved sand drop is 600 ft away. The final pedestrian route is dry but uphill.','The delivery truck cannot reach the school. The earliest sand drop is 1 hour after assignment; propose a safe last-mile plan.'),
('Protect the exposed side of a supply depot before the forecast shallow rise.','120 ft frontage; forecast water depth 6 in; possible fill staging 240 ft away.','This may require overnight work. Fill must be delivered; include lights, meals, rotation and verified power.'),
('Prioritize and plan protection at two sites sharing the same response resources.','Shelter: 30 ft affected entrance approach. Empty recreation building: 60 ft frontage, forecast water depth 6 in. Potential fill staging is 100 ft from shelter and 400 ft from recreation building.','Shelter request is due in 1 hour; recreation request in 3 hours. Protect people and essential access before empty property.')
]
for entry,revision in zip(sc,revisions):
 entry['mission'],entry['site'],entry['constraint']=revision
 # Keep legacy resource data out of the revised bank and editable data.
 for key in ['workers','shovels','equipment','bags','fill','materials']:
  entry.pop(key,None)
 entry['deadline']={1:2,2:4,3:2,4:2,5:1,6:3,7:4,8:1.5,9:2,10:3,11:12,12:2,13:4,14:4,15:3,16:4,17:4,18:4,19:12,20:3,21:1,22:1,23:2,24:1.5,25:2,26:1,27:4,28:4,29:12,30:3}[entry['id']]

# Shared references now describe quantities to request, rather than preallocated stock.
part1=[(t,b.replace("A card's listed stock is the initial allocation.","Scenario cards give requests and site constraints; students calculate the resources to request.").replace('Card stock default','Scenario resource requests').replace('Unless a card gives a delivery exception, allocated fill has already been delivered to the listed filling point; identify its delivery source and plan any resupply. Every card has basic PPE for its listed workers, one first-aid kit, closure supplies, a tape measure and access to a safe drinking-water refill source. Water containers, food and shade are not automatically supplied: request and schedule them.','No worker, bag, fill, equipment or PPE allocation is supplied on revised cards. Calculate and request each quantity, including drinking water, food, first aid, closure supplies and safe staging. State delivery and arrival assumptions. Equipment-specific approved ballast counts describe the mission requirement, not supplied stock.').replace('unless specifically authorized on the card','unless a qualified real-world design establishes otherwise')) for t,b in part1]
worksheet=[('PART 2 • RESPONSE ESTIMATE', """Name: ______________________ Team: ______ Scenario #: ____
Title: __________________________________________________
My measured bags in 20 min: ______  R = bags × 3: ______
Planning rate S: ______ bags/team-hour; factor: 0.75 / 0.50
Reason for factor and route adjustment: ____________________

Mission and chosen approach
What must be accomplished? ______________________________
Chosen structure or alternative: __________________________
Sketch with dimensions, layers, drainage, access and movement route:

[[SKETCH]]

Material estimate
Counting rule and calculation: ____________________________
____________________________________________________
Bags N (round up): ______; contingency if chosen: ___________
Fill N ÷ 75: ______ yd³; quarter-yard delivery order: ______ yd³
Other materials and dimensions: __________________________
For a basin: chosen depth ______; ft³ ______; gallons ______;
approximate water load ______ lb; freeboard/overflow: _______

Compare team counts
One team = 4 workers. Four teams = 16 workers.
One-team ideal time N ÷ S: ______ hours
Four-team ideal time N ÷ (4 × S): ______ hours
These estimates assume enough tools, safe space, fill and movement capacity.
Adjusted team-hours N ÷ S: ______
What could prevent four teams from being four times as fast?
____________________________________________________
____________________________________________________"""),('STAFFING & EQUIPMENT TO MEET THE REQUEST', """Name: ______________________ Scenario #: ______

Deadline and usable work time
Requested completion window: ______ hours
Delivery wait ______; setup/finish allowance ______ hours
Usable production time: ______ hours
Minimum teams = round up [N ÷ (S × usable hours)]: ______
Production workers = teams × 4: ______
Extra support workers and jobs: __________________________
Total people requested: ______
No usable time or unsafe mission? State the fallback: ________

Equipment and materials to request
Resource                        Quantity/capacity             Arrival/source
Shovels: ______________________________________________
Gloves and safety glasses: _______________________________
Movement equipment: ___________________________________
Fill delivery equipment/service: __________________________
Tarps/liners/fabric/other: _________________________________
Lights, radios, cones, first aid: ___________________________

Delivery, movement and actual schedule
Fill delivered from/to and expected arrival: _________________
Filled-bag route, trips and cycle time: _____________________
____________________________________________________
Operators and loading/placing workers: ____________________
How staffing avoids double-counting: ______________________
Schedule: task / start / finish / people and equipment
____________________________________________________
____________________________________________________
____________________________________________________
Final estimated elapsed time: ______ hours
Meets deadline? ______; limiting stage: ____________________

Worker support
Water stock plus reserve: ______ gal; cooler/refill plan: ______
Food needed / servings / timing: ___________________________
Rest and rotation: _______________________________________
Weather protection and first-aid contact: ___________________
Changes needed if deadline cannot be met: __________________"""),worksheet[2]]
# Retain the useful overview/background, but replace stock-based answer pages.
teacher=[(t,b) for t,b in teacher if not t.startswith('ESTIMATE GUIDE ')]
for i,(t,b) in enumerate(teacher):
 b=b.replace('Each scenario gives sufficient dimensions','Each scenario gives sufficient dimensions')
 b=b.replace('Every card gives sufficient dimensions for the shared counting rules.','Cards give mission dimensions. Students select and justify a classroom counting rule; there is no assigned structure or resource stock.')
 b=b.replace('Keep four workers, 20 minutes, route distance','Keep four workers, 20 minutes, route distance')
 b=b.replace('With only two shovels for three teams, accept using one production team plus helpers, requesting tools, or a clearly justified lower rate.','Students must request enough tools for their chosen workforce and explain any different allocation.')
 b=b.replace('A teacher may run another','A teacher may run another')
 b=b.replace('scenarios 11, 12, 15, 19, 27 and 30 deliberately demand redesign or rejection','scenarios 11, 12, 15, 19, 26, 27 and 30 invite comparison, redesign or rejection')
 teacher[i]=(t,b)
teacher.insert(3,('TEACHER GUIDE • REVISED REQUEST CARDS',"""The revised scenario cards intentionally omit supplied workers, equipment and materials, along with the long planning-question block. Students determine quantities instead of working backward from a fixed allocation. Counting rules remain in the separate common reference.

Required comparison
For chosen bag count N and sustained rate S, estimate one-team time N/S and four-team time N/(4S). These are ideal production-chain estimates. Then determine teams = round up [N/(S × usable hours)] to meet the request. Usable hours excludes unavoidable delivery delay and separate setup/finish allowance. Multiply production teams by four and add any separately staffed support roles.
Request shovels (starting point: two per team), gloves/glasses for every worker, fill, transport, other materials and worker support. Test whether the movement chain and workspace can support the chosen team count. Additional teams do not remove the delivery, space or safety constraint.

Judgment and alternatives
The following estimates illustrate reasonable classroom choices; they do not prescribe a structure. Lower narrow lines may suit shallow diversion, while a broad barrier may suit shallow standing water. Students must explain the choice and any changed mission. A narrow line is not automatically an adequate substitute for flood protection. Equipment station counts remain on relevant cards because they are approved mission requirements, not supplies.
No bag shortages are imposed in the initial cards. Resource limits can be introduced with incident updates against each student's own requested allocation. When an update refers to listed or available workers/equipment, apply it to the student's proposed resources. A safe redesign or rejection can earn full credit.

Deadline choices
Time windows range from 1 to 12 hours. A large request can require many teams; accept 12 four-person teams if the measured rate and feasible movement/support plan justify them. Do not cap staffing at the previous card allocations. Unsafe flood, slope, electrical or contaminated conditions cannot be solved solely by adding workers."""))
# Case-specific calculation examples remain flexible: normal/difficult alternatives use student's S.
for entry in sc:
 n=entry['n']; fill=n/75; idx=entry['id']
 option='Example only: use the common reference rule appropriate to a justified layout. The earlier baseline count below is not the only acceptable estimate.'
 if idx in [1,3,4,5,6,7,8,9,28,30]: option='A narrow two-layer diversion line is one classroom option for shallow runoff. Justify the route and receiving drainage; choose another count if the mission/layout changes.'
 elif idx in [2,10,11,12,29]: option='A broad three-layer shallow barrier is one classroom option, with returns included or separately estimated. Check forecast depth and leakage. Card 12 is unsafe as a road defense regardless of staffing.'
 elif idx in [13,14,15,16,17]: option='A small two-wide, two-layer erosion-control line is one counting option for each affected section, subject to qualified approval. It is not slope, road or bank reinforcement.'
 elif idx in [18,19,20]: option='A two-wide, two-layer perimeter is a starting option for a shallow basin. Card 19 uses a hypothetical four-wide/four-layer count to expose why the requested depth is still infeasible. Safer reduced depths or approved containers are valid alternatives.'
 elif idx in [21,25]: option='The reference ground-cover rule is one bag per 4 ft of perimeter. This is an inventory estimate for light conditions, not a wind rating.'
 elif idx in [22,23,24]: option='Use the supervisor-specified approved stations × bags per station. The equipment still requires rated supports and required anchors.'
 elif idx==26: option='One illustrative narrow three-layer line uses 3 bags/ft. Responders may instead require another containment method; ordinary teams have no authority to enter contamination.'
 elif idx==27: option='One illustrative broad three-layer line uses 6 bags/ft. Real containment method, compatibility and deployment are responder decisions.'
 notes=entry['reason']+' '+entry['extra']+'.'
 if idx in [18,19,20]:
  length,width,depth={18:(12,8,.5),19:(30,20,2),20:(10,10,.25)}[idx]
  volume=length*width*depth; gallons=volume*7.48
  notes+=f' Requested basin volume at {depth:g} ft depth: {volume:g} ft³, {gallons:.2f} gallons, approximately {gallons*8.3:,.0f} lb of water. Recalculate for a safer selected operating depth; stored water is not guaranteed rainwater supply.'
 # Stock-era transport notes are deliberately replaced with request-based capacity checks.
 teacher.insert(4+idx-1,(f"ESTIMATE GUIDE {idx:02d} • {entry['title']}",f"""Possible approach, not a prescribed solution
{option}

Illustrative estimate
{n:,} bags; fill = {n}/75 = {fill:.2f} yd³; quarter-yard order {math.ceil(fill*4)/4:.2f} yd³. Allow justified return/corner or contingency changes. Student must show the actual selected rule and dimensions.

One team, four teams and deadline staffing
S = 0.75R normally, or 0.50R for justified difficult conditions.
One-team time: {n}/S hours; four-team time: {n}/(4S) hours.
Adjusted team-hours: {n}/S. Deadline: {entry['deadline']:g} hours.
Minimum production teams: round up [{n}/(S × usable hours)]. Delivery delay/route constraints: {entry['constraint']}
For illustration only, if R = 60 then normal S = 45: one team {n/45:.2f} h; four teams {n/180:.2f} h. Deadline lower bound ignoring setup/delivery is {math.ceil(n/(45*entry['deadline']))} teams. Substitute the student's measured R and actual usable time.

Equipment and actual elapsed time
Start with 2 shovels per production team and one gloves/glasses set per worker, including support workers. Request fill delivery, appropriate moving equipment, closure tools, first aid, water and other materials. Check the route against trial distance.
On a dry level route ≤300 ft, each separately staffed wheelbarrow moves at most 24 bags/h and each cart 48 bags/h under catalog assumptions; longer or difficult routes are slower. Round trips up and include operators/loading help. Vehicle access is not guaranteed. Equipment requests must match the chosen number of teams rather than assumed fixed card stock.

Major constraints and judgment
{notes}
Students should identify the likely slowest stage, actual completion time, safe access/drainage, material dimensions, drinking-water delivery, rest/rotation and food for longer work. Accept fewer bags only when a reduced mission is explicit; accept more teams only with equipment, safe workspace and support to use them."""))

scenario_pages=[]
for entry in sc:
 deadline=f"Complete within {entry['deadline']:g} hours of assignment."
 if entry['id']==30: deadline='Shelter: within 1 hour. Recreation building: within 3 hours.'
 body=f"""ZOMBIE INVASION PREP / EMERGENCY RESPONSE EXERCISE
CLASSROOM SIMULATION • OPERATIONS REQUEST

SITUATION
{entry['situation']}

REQUEST
{entry['mission']}

SITE INFORMATION
{entry['site']}

CONDITIONS
{entry['weather']}.

REQUESTED TIME WINDOW
{deadline} Delivery, setup and finishing count toward the time window.

OPERATIONAL CONSTRAINT
{entry['constraint']}

ESTIMATE TO SUBMIT
Bags and fill required • Time with 1 team • Time with 4 teams
Teams, people and equipment needed to meet the requested window
Use your measured rate and the common reference. State your chosen approach and assumptions; recommend a change if the request is impractical.

PLANNER: __________________________  TEAM RATE: __________
CLASSROOM EXERCISE — NOT A REAL DEPLOYMENT ORDER"""
 scenario_pages.append((f"REQUEST {entry['id']:02d} / {entry['title'].upper()}",body))

write('01-student-basic-calculation-packet',part1)
write('00-basic-calculation-sheet-only',[part1[1]])
write('02-student-operational-planning-worksheet',worksheet)
write('03-student-scenario-bank',scenario_pages)
write('05-teacher-guide-and-estimates',teacher)
# Cuttable incident cards, four per page.
upd_story=[]
for i in range(0,len(updates),4):
 if i: upd_story.append(PageBreak())
 upd_story.append(Paragraph(f'INCIDENT UPDATES {i+1:02d}–{min(i+4,len(updates)):02d}',styles['PageTitle']))
 rows=[]
 for j,(title,desc) in enumerate(updates[i:i+4],i+1):
  card=[Paragraph(f'UPDATE {j:02d} / {html.escape(title.upper())}',styles['SectionClean']),Paragraph(html.escape(desc),styles['CardText']),Paragraph('Revise your resources, staffing, schedule, worker support and operational decision. Show what changes and why.',styles['CardText'])]
  rows.append([card])
 table=Table(rows,colWidths=[528],rowHeights=[155]*len(rows))
 table.setStyle(TableStyle([('BOX',(0,0),(-1,-1),.7,colors.HexColor('#607680')),('INNERGRID',(0,0),(-1,-1),.5,colors.HexColor('#8d9aa0')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),9)]))
 upd_story.append(table)
SimpleDocTemplate(str(OUT/'04-incident-update-cards.pdf'),pagesize=letter,rightMargin=42,leftMargin=42,topMargin=40,bottomMargin=48).build(upd_story,onFirstPage=footer,onLaterPages=footer)
(OUT/'04-incident-update-cards.md').write_text('\n\n---\n\n'.join(f'# UPDATE {i:02d} / {t}\n\n{d}\n\nRevise resources, staffing, schedule, worker support and decision.' for i,(t,d) in enumerate(updates,1)))
from creative_missions import build as build_creative_missions
creative_pages = build_creative_missions(OUT, write)
all_pages=part1+worksheet+scenario_pages+[(f'UPDATE {i:02d} / {t}',d) for i,(t,d) in enumerate(updates,1)]+teacher
(OUT/'complete-editable-package.md').write_text('\n\n---\n\n'.join('# '+t+'\n\n'+b for t,b in all_pages + creative_pages))
(OUT/'scenario-data.json').write_text(json.dumps(sc,indent=2))
(OUT/'README.md').write_text('''# Sandbag Emergency Logistics Exercise

Two-part student activity with separate teacher materials.

- **00**: Standalone one-page data and basic calculation sheet.
- **01**: 5-page calculation packet. Pages 1–2 per team; pages 3–5 common references per student.
- **02**: 3-page individual planning worksheet, one per student.
- **03**: 30 one-page open-ended operations request cards; estimate bags/fill, one-team time, four-team time, and deadline staffing/equipment. No preallocated workers, equipment or materials.
- **04**: 24 incident-update cards, four per page on 6 pages; cut along rules.
- **06**: 12 dramatic engineering mission cards (requests 31–42), using the original calculation method.
- **07**: Separate creative-mission teacher estimates, engineering extensions and mission-specific incident updates.
- **05**: Teacher overview, protocol, safety, calculation guidance, one estimate page for each scenario, debrief and sources.

All PDFs use US Letter. Matching Markdown files provide editable text. `complete-editable-package.md` contains all sections. `scenario-data.json` contains structured card data. `build_sandbag_package.py` and `creative_missions.py` rebuild the PDFs using Python and ReportLab; change OUT if relocating the folder.

No scale or bag-weight calculation is required. Do not mistake classroom assumptions for real engineering specifications. The field activity is a supervised, dry-site production trial; emergency scenarios are paper planning exercises.
''')
import shutil
source_path=Path(__file__).resolve()
if source_path != (OUT/'build_sandbag_package.py').resolve():
 shutil.copyfile(source_path,OUT/'build_sandbag_package.py')
print(f'Created {len(sc)} scenarios, {len(updates)} updates; PDFs and editable sources in {OUT}')
