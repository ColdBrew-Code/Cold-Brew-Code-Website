document.addEventListener('DOMContentLoaded', () => {
  const carousels = document.querySelectorAll('[data-carousel]');

  carousels.forEach((carousel) => {
    const track = carousel.querySelector('[data-carousel-track]');
    const slides = Array.from(carousel.querySelectorAll('[data-carousel-slide]'));
    const previousButton = carousel.querySelector('[data-carousel-prev]');
    const nextButton = carousel.querySelector('[data-carousel-next]');
    const dots = Array.from(carousel.querySelectorAll('[data-carousel-dot]'));
    const status = carousel.querySelector('[data-carousel-status]');

    if (!track || slides.length < 2) {
      return;
    }

    let activeIndex = 0;

    const updateCarousel = (nextIndex) => {
      activeIndex = (nextIndex + slides.length) % slides.length;

      track.style.transform = `translateX(-${activeIndex * 100}%)`;

      slides.forEach((slide, slideIndex) => {
        const isActive = slideIndex === activeIndex;
        slide.classList.toggle('is-active', isActive);
        slide.setAttribute('aria-hidden', isActive ? 'false' : 'true');
      });

      dots.forEach((dot, dotIndex) => {
        const isActive = dotIndex === activeIndex;
        dot.classList.toggle('is-active', isActive);
        dot.setAttribute('aria-current', isActive ? 'true' : 'false');
        dot.setAttribute('aria-label', isActive
          ? `Slide ${dotIndex + 1} of ${slides.length}, current slide`
          : `Show slide ${dotIndex + 1} of ${slides.length}`);
      });

      if (status) {
        status.textContent = `Slide ${activeIndex + 1} of ${slides.length}`;
      }
    };

    previousButton?.addEventListener('click', () => updateCarousel(activeIndex - 1));
    nextButton?.addEventListener('click', () => updateCarousel(activeIndex + 1));

    dots.forEach((dot, dotIndex) => {
      dot.addEventListener('click', () => updateCarousel(dotIndex));
    });

    carousel.addEventListener('keydown', (event) => {
      if (event.key === 'ArrowLeft') {
        event.preventDefault();
        updateCarousel(activeIndex - 1);
        return;
      }

      if (event.key === 'ArrowRight') {
        event.preventDefault();
        updateCarousel(activeIndex + 1);
        return;
      }

      if (event.key === 'Home') {
        event.preventDefault();
        updateCarousel(0);
        return;
      }

      if (event.key === 'End') {
        event.preventDefault();
        updateCarousel(slides.length - 1);
      }
    });

    updateCarousel(0);
  });
});