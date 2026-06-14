function openSwiper(index) {

    const lightbox = document.getElementById("lightbox");
    lightbox.style.display = "block";

    if (!swiper) {
        swiper = new Swiper('.mySwiper', {
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            keyboard: {
                enabled: true,
            }
        });
    }

    setTimeout(() => {
        swiper.update();
        swiper.slideTo(index, 0);
    }, 50);
}