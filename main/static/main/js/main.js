let owl = $('.owl-carousel');
owl.owlCarousel({
    dots:false,
    items: 3,
    margin: 30,
    loop:true,
    autoplay: true

});

$('.customNextBtn').click(function() {
    owl.trigger('next.owl.carousel');
});
$('.customPrevBtn').click(function() {
    owl.trigger('prev.owl.carousel', [300]);
});

$(document).ready(function () {
    $('.owl-carousel').owlCarousel({
        interval: 3000 });
    $('.owl-carousel').owlCarousel('cycle'); });
