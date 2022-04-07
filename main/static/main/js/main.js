let owl = $('.owl-carousel');
owl.owlCarousel({
    items: 3,
    margin: 30,
    autoHeight: true,
    dotsContainer: '#dots',
    loop:true,
    responsive : {
        768 : {
            items: 2
        },
        300 : {
            items: 1,
            stagePadding: 50
        }
    }

});
$('.owl-next').click(function() {
    owl.trigger('next.owl.carousel');
});

$('.owl-prev').click(function() {
    owl.trigger('prev.owl.carousel', [300]);
});

$('.owl-dot').click(function () {
    owl.trigger('to.owl.carousel', [$(this).index(), 300]);
});
