     $(window).scroll(function () {
            if ($(this).scrollTop() > 550) {
                console.log("Vatsal")
                $('#Nav').addClass('fixed-top');
            } else {
                $('#Nav').removeClass('fixed-top');
            }
        });
