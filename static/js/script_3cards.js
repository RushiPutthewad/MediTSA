
document.getElementById("showPopup").addEventListener("click", function() {
    document.getElementById("popupContainer").classList.add("active");
    setTimeout(() => {
        document.getElementById("card1").style.animation = "fadeInCard1 0.5s forwards";
    }, 100);
    setTimeout(() => {
        document.getElementById("card2").style.animation = "fadeInCard2 0.5s forwards";
    }, 300);
    setTimeout(() => {
        document.getElementById("card3").style.animation = "fadeInCard3 0.5s forwards";
    }, 500);
});

// Close popup when clicking outside of cards
document.getElementById("popupContainer").addEventListener("click", function(event) {
    if (!event.target.closest(".popup-card")) {
        document.getElementById("popupContainer").classList.remove("active");
    }
});