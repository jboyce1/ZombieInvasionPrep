(function () {
  "use strict";

  const launch = document.getElementById("valley-launch");
  const presentation = document.getElementById("valley-presentation");
  const slide = document.getElementById("valley-slide");
  const exit = document.getElementById("valley-exit");
  const status = document.getElementById("valley-status");

  if (!launch || !presentation || !slide || !exit || !status) return;

  const slideRoot = presentation.dataset.slideRoot;
  const slideCount = Number(presentation.dataset.slideCount);
  const presentationName =
    presentation.dataset.presentationName || "Uncanny Valley presentation";
  let currentSlide = 0;
  let isOpen = false;

  function slideUrl(number) {
    return `${slideRoot}/slide-${String(number).padStart(2, "0")}.jpg`;
  }

  function showSlide(number) {
    currentSlide = Math.max(0, Math.min(number, slideCount));

    if (currentSlide === 0) {
      slide.removeAttribute("src");
      slide.classList.add("is-black");
      slide.alt = "Black opening slide";
      status.textContent = "Black opening slide";
      return;
    }

    slide.src = slideUrl(currentSlide);
    slide.classList.remove("is-black");
    slide.alt = `${presentationName} slide ${currentSlide} of ${slideCount}`;
    status.textContent = `Slide ${currentSlide} of ${slideCount}`;

    if (currentSlide < slideCount) {
      const nextSlide = new Image();
      nextSlide.src = slideUrl(currentSlide + 1);
    }
  }

  function openPresentation() {
    isOpen = true;
    showSlide(0);
    presentation.hidden = false;
    document.body.style.overflow = "hidden";
    presentation.focus({ preventScroll: true });

    const requestFullscreen =
      presentation.requestFullscreen || presentation.webkitRequestFullscreen;
    if (requestFullscreen) {
      const result = requestFullscreen.call(presentation);
      if (result && typeof result.catch === "function") result.catch(() => {});
    }
  }

  function closePresentation() {
    if (!isOpen) return;
    isOpen = false;
    presentation.hidden = true;
    document.body.style.overflow = "";
    slide.removeAttribute("src");
    launch.focus({ preventScroll: true });

    const fullscreenElement =
      document.fullscreenElement || document.webkitFullscreenElement;
    const exitFullscreen =
      document.exitFullscreen || document.webkitExitFullscreen;
    if (fullscreenElement && exitFullscreen) {
      const result = exitFullscreen.call(document);
      if (result && typeof result.catch === "function") result.catch(() => {});
    }
  }

  launch.addEventListener("click", openPresentation);

  presentation.addEventListener("click", function () {
    if (currentSlide < slideCount) showSlide(currentSlide + 1);
  });

  exit.addEventListener("click", function (event) {
    event.stopPropagation();
    closePresentation();
  });

  document.addEventListener("keydown", function (event) {
    if (!isOpen) return;

    if (["ArrowRight", " ", "Enter", "PageDown"].includes(event.key)) {
      event.preventDefault();
      if (currentSlide < slideCount) showSlide(currentSlide + 1);
    } else if (["ArrowLeft", "Backspace", "PageUp"].includes(event.key)) {
      event.preventDefault();
      showSlide(currentSlide - 1);
    } else if (event.key === "Escape") {
      closePresentation();
    }
  });

  function handleFullscreenChange() {
    const fullscreenElement =
      document.fullscreenElement || document.webkitFullscreenElement;
    if (isOpen && !fullscreenElement) closePresentation();
  }

  document.addEventListener("fullscreenchange", handleFullscreenChange);
  document.addEventListener("webkitfullscreenchange", handleFullscreenChange);
}());
