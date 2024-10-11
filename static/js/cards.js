const carouselInner = document.querySelector('.carousel-inner');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
const cards = document.querySelectorAll('.card');

let counter = 0;
const cardWidth = cards[0].offsetWidth + 20; // Consider margin-right

nextBtn.addEventListener('click', () => {
    counter = (counter + 1) % cards.length;
    carouselInner.style.transform = `translateX(${-counter * cardWidth}px)`;
});

prevBtn.addEventListener('click', () => {
    counter = (counter - 1 + cards.length) % cards.length;
    carouselInner.style.transform = `translateX(${-counter * cardWidth}px)`;
});