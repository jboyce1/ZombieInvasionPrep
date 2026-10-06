"""Additional mission cards. All dimensions and performance figures are classroom assumptions."""
import math
import json

# title, story, request, site, deadline, constraint, example count, reasoning, twist
MISSIONS = [
('Last Signal Before Dark',
 'The evacuation convoy is waiting for a route update. The relay radio has one battery left, and the road crew cannot hear headquarters. A technician has proposed a creek-powered charging station.',
 'Plan a shallow diversion intake for a technician-operated microhydro unit. Decide whether it can sustain a 25 W charging demand.',
 'A proposed U-shaped intake has a 12 ft front and two 6 ft returns. Fill staging is 180 ft away on a dry level path. An existing downhill pipe route provides 5 m of drop; flow is 2 L/s. Assume 40% overall efficiency, including losses. Power estimate: watts = 9.81 × flow (L/s) × drop (m) × efficiency.',
 3, 'The drop comes from the terrain, not a tall sandbag dam. Request screened intake, pipe, turbine, generator and charging controls; a qualified adult handles installation. Show a safe bypass and a battery fallback.',
 48, 'Illustrative narrow two-layer intake: (12 + 6 + 6) × 2 = 48. Power = 39.24 W, nominally above 25 W; this does not guarantee charging reliability.',
 'Leaves cut usable flow to 1 L/s. Recalculate power and decide which communications loads stay on.'),
('The Wheel That Keeps Turning',
 'The fuel shed is empty. At the shelter garden, seed trays are drying while a small mechanical irrigation pump sits idle. An old demonstration water wheel could drive it through a guarded belt.',
 'Plan the intake and channel for a technician-approved wheel system; keep the garden watered without an electric motor.',
 'Proposed U intake: 8 ft front and two 4 ft returns. Two lined channel edges are each 15 ft long. Fill staging is 90 ft away. Use a supplied demonstration rating of 12 pump strokes/minute and 0.20 gallon/stroke. The garden needs 180 gallons.',
 4, 'Request wheel, frame, bearings, guarded drive, pump and liner. Sandbags shape water delivery; they are not wheel bearings or machine supports. Keep the bypass open and rotating parts inaccessible.',
 92, 'Intake: 16 × 2 = 32; channel edges: 30 × 2 = 60; total 92. Assumed delivery = 2.4 gal/min; 180 gallons requires 75 minutes after commissioning.',
 'A branch jams the screen. Flow stops for 30 minutes; revise the watering schedule and inspection staffing.'),
('Water Must Climb the Hill',
 'The hilltop food garden is the shelter’s next harvest. Its irrigation tank is empty, the generator has failed, and carrying buckets up the hill will pull workers away from evacuation support.',
 'Plan a shallow intake for a proper hydraulic ram pump and estimate whether it can deliver 120 gallons within four operating hours.',
 'Proposed U intake: 10 ft front and two 5 ft returns. Fill staging is 240 ft away on level ground. Source flow through the drive pipe is 6 gal/min; fall to pump is 4 ft; lift from pump to tank is 24 ft. Assume efficiency 0.60. Delivery gal/min = efficiency × source flow × fall ÷ lift.',
 3, 'Construction window is separate from four operating hours. Request ram pump, drive pipe, delivery pipe, screened intake and a rated tank. Plan return drainage for water not pumped uphill; do not create an improvised elevated reservoir.',
 40, 'Intake: 20 × 2 = 40 bags. Estimated delivery = 0.6 gal/min; four hours gives 144 gallons; 120 gallons takes 200 minutes.',
 'Source flow falls to 3 gal/min. Recalculate supply and choose a backup or reduced watering target.'),
('Thirty People, One Working Toilet',
 'The shelter toilets still work, but the water main is down. Thirty evacuees arrive before the next tanker. Rain is forecast, and staff want reserve flushing water ready before the roof begins shedding runoff.',
 'Plan roof-runoff collection into a shallow lined basin for nonpotable flushing water.',
 'Proposed basin inside dimensions: 12 × 8 ft; operating water depth 0.25 ft. Roof collection area is 600 ft². Forecast rainfall is 0.5 in; assume 80% collection efficiency. Expected runoff ft³ = roof area × rainfall in feet × efficiency. Demand: 30 people × 2 flushes × 1.5 gallons.',
 2, 'Ground-level site; fill staging 80 ft away. Request gutters, screen, liner and transfer containers. Keep overflow away from the shelter. No roof access by students; forecast rain is not water already in storage.',
 160, 'Perimeter 40 ft × 4 = 160. Capacity = 24 ft³ = 179.52 gal. Forecast harvest = 20 ft³ = 149.60 gal; demand = 90 gal. Both quantities exceed demand under assumptions, but rainfall timing and transfer still matter.',
 'Only 0.2 in of rain arrives. Recalculate harvest and the tanker quantity still needed.'),
('Catch the Rain Before It Vanishes',
 'The shelter roof cannot be used: a fallen branch damaged the gutters. A passing shower may be the only chance to collect water for the garden before the heat returns.',
 'Plan a supported tarp catchment feeding a shallow lined basin and keep the collection route from collapsing or overflowing.',
 'Catchment tarp is 16 × 12 ft; supplied approved ground-edge anchoring plan uses 18 bag stations with 2 bags each. Basin inside dimensions: 8 × 6 ft at 0.25 ft operating depth. Forecast rainfall: 0.75 in; collection efficiency: 70%. Garden request: 50 gallons. Fill staging is 120 ft away.',
 3, 'Request suitable tarp supports, gutter/hose, screen and liner. The station count applies only to the supplied support plan; no improvised overhead water loads. Forecast yield = area × rainfall in feet × efficiency × 7.48.',
 148, 'Anchors = 36; basin = 28 × 4 = 112; total 148. Basin capacity 89.76 gal; forecast yield 62.832 gal, nominally above 50.',
 'A tear reduces collection efficiency to 40%. Estimate the shortfall and plan repair time.'),
('Mud Is Killing the Pump',
 'The shelter’s cleanup pump is choking on grit. Volunteers keep clearing the intake, but muddy runoff returns faster than they can work. A second cleanout would stop the cleanup line.',
 'Plan two shallow lined settling cells so one can be isolated and cleaned while the other remains available.',
 'Each separate cell is 10 × 6 ft inside, with 0.25 ft operating depth. Cells have separate full perimeters. A further 12 ft two-layer line routes clean upslope rainwater around the station. Fill staging is 200 ft away. Assume an operating inflow of 3 gal/min.',
 4, 'Request two liners, controlled outlets, isolation valves, screens and sediment tools. Settling is pretreatment; transferred water remains nonpotable. Show isolated-cell drainage and an overflow route.',
 280, 'Two perimeters: 2 × 32 × 4 = 256; diversion = 12 × 2 = 24; total 280. Each cell holds 112.2 gal; volume ÷ inflow = 37.4 min nominal residence time, not a sediment-removal guarantee.',
 'One cell must be taken offline and inflow doubles. Recalculate nominal residence time and decide whether to pause transfer.'),
('The Slick at the Drain',
 'A shiny slick is drifting toward the shelter’s drainage outlet. Blocking all the water would flood the loading area; letting it all through could carry the slick downstream.',
 'Prepare a paper plan for responder-controlled underflow containment: retain floating material while providing a submerged water outlet.',
 'Proposed U containment footprint: 14 ft front and two 7 ft returns. Use a shallow 0.25 ft planning water depth and a two-wide, two-layer perimeter. Fill staging is 100 ft outside the exclusion zone. Hypothetical inflow is 8 gal/min; approved outlet rating is 10 gal/min.',
 2, 'Qualified responders specify liner, outlet geometry and recovery equipment. Do not invent an outlet opening from bag counts. Underflow does not purify water. A student demonstration uses only a contained tray and vegetable oil.',
 112, 'Perimeter = 28 ft; 28 × 4 = 112 bags. Rated outlet exceeds inflow by 2 gal/min under the stated assumptions; no separation efficiency follows from that comparison.',
 'Debris reduces outlet capacity to 5 gal/min. Calculate net accumulation over 20 minutes; call for isolation/recovery rather than releasing the slick.'),
('Keep the Dirty Water Out',
 'Cleanup crews have isolated a contaminated loading pad. A new storm is about to send clean hillside runoff into it, multiplying the volume responders must collect.',
 'Plan a clean-water diversion outside the exclusion zone and request support for a lined washwater collection pad inside the responder work area.',
 'Clean diversion route is 36 ft with two 8 ft returns. Separate washwater pad inside dimensions: 10 × 8 ft at 0.25 ft operating depth. Washwater production is 2 gal/min for 60 minutes. Fill staging is 150 ft away on an approved clean route.',
 3, 'Students estimate resources; responders deploy inside the exclusion zone and choose compatible liner and recovery method. Clean runoff must reach approved drainage. Keep contaminated collection and drinking-water supplies separate.',
 248, 'Diversion: 52 × 2 = 104; collection pad: 36 × 4 = 144; total 248. Pad capacity = 149.6 gal; washwater = 120 gal, leaving 29.6 gal before the operating-depth limit.',
 'The wash runs for 90 minutes instead. Calculate the recovery volume needed to prevent exceeding the operating-depth limit.'),
('The Repair Window Is Closing',
 'A shutoff valve in a shallow service yard is leaking. The technician can fix it if the immediate work area stays dry, but runoff will return when the next shower arrives.',
 'Plan a small surface repair pocket, pumping and discharge protection; give the technician a usable work window.',
 'Proposed U pocket: 12 ft front and two 8 ft returns. Separately specified discharge apron has 24 ft of ground-cover perimeter. Fill staging is 60 ft away. Scenario pump capacity: 6 gal/min; seepage: 2 gal/min. Initial removable water is 40 gallons.',
 2, 'Request liner, pump, screened intake and erosion-control apron. No excavation, trenches or underground entry. Route pumped water to approved drainage. Pumping time begins after installation; maintain access and electrical controls.',
 118, 'Pocket = 28 × 4 = 112; apron anchors = ceiling(24/4) = 6; total 118. Net pumping = 4 gal/min; initial drawdown takes 10 minutes under constant assumptions.',
 'Seepage rises to 7 gal/min. Explain why more bags or the original pump alone do not provide a dry repair window.'),
('The Dark-Sky Aid Station',
 'A mobile aid station must stay open through sunset. Its radios, charging tent and ground-mounted solar unit all need setup, while runoff is heading for the equipment area.',
 'Plan bags and staffing for approved equipment ballast, ground-cover anchors and shallow runoff diversion before patient arrivals.',
 'Approved tent plan: 8 stations × 4 bags. Approved low solar-frame plan: 6 stations × 3 bags. Ground supply cover: 12 × 8 ft, one bag per 4 ft of perimeter. Runoff line: 30 ft plus two 5 ft returns. Fill staging is 280 ft away. Tasks can use separately staffed work zones.',
 2, 'Request manufacturer-specified frames, anchors and attachments, lighting and safe power connections. Bag counts do not establish a wind rating. Keep routes accessible and protect supplies on approved platforms.',
 140, 'Tent 32 + solar 18 + cover 10 + diversion 80 = 140 bags. Students must allocate teams by dependency and check cart capacity over the longer route.',
 'A thunderstorm warning ends outdoor operation. Reassign the plan to an indoor aid station and account for safe retrieval time.'),
('The Last Dry Supply Lane',
 'Relief supplies arrive in two hours. The receiving area is wet, and a muddy path separates the delivery point from the shelter. Food boxes cannot sit in runoff while workers argue about where to put them.',
 'Plan shallow diversion, anchored ground fabric and a lined boot-cleaning tray to keep a dry supply route operating.',
 'Diversion route: 28 ft plus two 6 ft returns. Ground-fabric path: 24 × 4 ft; use one bag per 4 ft of perimeter. Boot tray inside dimensions: 6 × 4 ft at 0.25 ft operating depth. Fill staging is 160 ft away; a 6 ft accessible entrance must stay clear.',
 2, 'Request traction surface, approved decking/pallets, ground fabric, tray liner, brushes and washwater containers. Bags anchor edges outside walking paths; bags themselves are not stepping stones or deck supports.',
 174, 'Diversion 40 × 2 = 80; path anchors ceiling(56/4) = 14; tray 20 × 4 = 80; total 174. Tray capacity 44.88 gal; captured muddy water needs removal.',
 'The delivery truck cannot reach the planned unloading area. Filled bags and supplies now travel 450 ft; revise cart cycles, staffing and arrival time.'),
('Four Calls, One Crew',
 'Dispatch receives four urgent calls at once: the radio needs power, toilets need flushing water, muddy runoff threatens the drain, and the aid tent cannot open. Every caller says their job comes first.',
 'Submit one coordinated plan for four work zones, with priorities, dependencies and a defensible reduced-service fallback.',
 'Radio U intake: 8 ft front + two 4 ft returns. Flushing basin: 10 × 6 ft inside at 0.25 ft depth. Mud diversion: 24 ft + two 6 ft returns. Approved aid-tent ballast: 6 stations × 4 bags. Fill staging is central; routes to the four zones are 60, 180, 300 and 420 ft respectively.',
 3, 'Initial card gives no supplied crew or stock: calculate and request them. A technician supplies the power-system design; responders approve water routes and tent plan. Preserve shelter access. Explain which jobs can proceed in parallel.',
 256, 'Intake 16 × 2 = 32; basin 32 × 4 = 128; diversion 36 × 2 = 72; tent 24; total 256. Basin capacity = 112.2 gal. Route-specific transport may dominate the schedule.',
 'After your request is submitted, dispatch can deliver only 60% of your requested empty bags, rounded down, and half your requested production teams, rounded down. Prioritize, resize or relocate; calculate the revised service level.')
]

def build(out, write):
    student=[]; teacher=[]; data=[]
    for i, row in enumerate(MISSIONS,31):
        title,story,request,site,deadline,constraint,n,reason,twist=row
        body=f'''ZOMBIE INVASION PREP / EMERGENCY RESPONSE EXERCISE
CLASSROOM SIMULATION • OPERATIONS REQUEST

SITUATION
{story}

REQUEST
{request}

SITE INFORMATION
{site}

REQUESTED TIME WINDOW
Complete construction within {deadline} hours of assignment. Delivery, setup, inspection and finishing count. State weather/daylight assumptions and choose your planning factor.

OPERATIONAL CONSTRAINT
{constraint}

ESTIMATE TO SUBMIT
Use the existing worksheet and your measured rate: bags and fill; time with 1 team and 4 teams; teams, people, equipment and worker support to meet the deadline. Choose and justify a counting rule; include water routing, access, and overflow or equipment-failure fallback. Engineering performance checks are an extension after the core estimate.

PLANNER: _____________________ TEAM RATE: __________
CLASSROOM EXERCISE — NOT A REAL DEPLOYMENT ORDER'''
        student.append((f'REQUEST {i:02d} / {title.upper()}',body))
        fill=n/75
        teacher.append((f'ESTIMATE {i:02d} / {title.upper()}',f'''POSSIBLE APPROACH • NOT A PRESCRIBED DESIGN
{reason}

CORE CALCULATIONS
Illustrative N = {n} bags; fill = {n}/75 = {fill:.2f} yd³; quarter-yard order = {math.ceil(fill*4)/4:.2f} yd³. Add justified corners, returns or contingency and recalculate if the layout changes.
R = measured completed bags in 20 minutes × 3. Choose S = 0.75R or 0.50R, with justification. One-team time = {n}/S; four-team time = {n}/(4S). Usable hours = {deadline} minus delivery wait and separate setup/finish time. Minimum teams = round up [{n}/(S × usable hours)]; production workers = teams × 4. If usable time is zero or negative, change the plan.
Practice example only: R = 60, S = 45 gives {n/45:.2f} hours for one team and {n/180:.2f} hours for four teams. Actual staffing uses the student's rate and usable time.

RESOURCE AND SCHEDULE CHECK
Request empty bags, fill, delivery, two shovels per team as a starting point, gloves/glasses for every worker, appropriate transport and separately staffed support. Use the existing catalog's trips and route cycle times. Do not double-count movement already in the trial. Include technicians and inspections in dependencies, plus drinking water, rest, food when applicable and first aid. Additional bags cannot replace the listed machinery or qualified design.

INCIDENT UPDATE • ISSUE AFTER THE INITIAL PLAN
{twist}

ASSESSMENT
Require recalculated quantities and a revised schedule, service level and fallback. Accept justified alternative layouts. Keep engineering extensions distinct from the measured sandbag production rate.'''))
        data.append(dict(id=i,title=title,situation=story,mission=request,site=site,deadline=deadline,constraint=constraint,illustrative_bags=n,estimate_notes=reason,incident_update=twist))
    intro=('CREATIVE MISSIONS / TEACHER NOTES', '''HOW TO USE
Requests 31–42 extend the original 30 cards. Give each student one request plus the existing 01 common references and 02 operational worksheet. Keep teacher estimates and mission-specific incident updates separate until the initial estimate is submitted. All missions retain the measured four-worker, 20-minute production method, fill conversion and one-team/four-team/deadline comparisons. No initial crew, equipment or material allocation is supplied; required station counts are mission requirements.

ENGINEERING EXTENSIONS
Performance figures are explicit hypothetical assumptions, not equipment guarantees. Have students complete the original logistics calculations first. Use gallons = ft³ × 7.48; rainfall in feet = inches ÷ 12. Basin capacity assumes the stated operating depth, not the crest. Report freeboard and overflow; add liner dimensions, corners and contingency where justified. The common reference's water-load estimate remains available; no sandbag weighing is required.

FIELD FORMAT
Keep the original supervised dry-site filling/closing/carrying/placement trial. These larger systems are paper missions. Optional tabletop demonstrations use shallow contained clean water and adult-operated apparatus. Qualified adults handle machinery and electrical systems; responders handle actual contamination. Real stream alterations and water-retaining structures require qualified review. Inspection and replacement are part of long-outage plans.

SOURCES AND ASSUMPTIONS
DOE explains that hydropower depends on flow and elevation drop and uses turbines/generators: https://www.energy.gov/cmei/water/how-hydropower-works
NC State Extension describes ram pumps and the efficiency × source flow × fall/lift estimate: https://content.ces.ncsu.edu/hydraulic-ram-pumps
EPA discusses containment/diversion, liners and overflow/underflow methods: https://www.epa.gov/emergency-response-research/stormwater-decontamination-containment-and-diversion-technologies
All mission dimensions, deadlines, loads, rainfall, machine ratings and incident changes were created for this exercise. Sources support the underlying functions, not these classroom layouts.''')
    write('06-creative-field-missions',student)
    write('07-creative-missions-teacher-guide',[intro]+teacher)
    (out/'creative-mission-data.json').write_text(json.dumps(data,indent=2)+'\n')
    return student+[intro]+teacher
