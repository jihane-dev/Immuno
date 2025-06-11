
(function ($) {

  "use strict";

  // MENU
  $('.navbar-collapse a').on('click', function () {
    $(".navbar-collapse").collapse('hide');
  });

  // CUSTOM LINK
  $('.smoothscroll').click(function () {
    var el = $(this).attr('href');
    var elWrapped = $(el);
    var header_height = $('.navbar').height();

    scrollToDiv(elWrapped, header_height);
    return false;

    function scrollToDiv(element, navheight) {
      var offset = element.offset();
      var offsetTop = offset.top;
      var totalScroll = offsetTop - navheight;

      $('body,html').animate({
        scrollTop: totalScroll
      }, 300);
    }
  });

  $(window).on('scroll', function () {
    function isScrollIntoView(elem) {
      var docViewTop = $(window).scrollTop();
      var docViewBottom = docViewTop + $(window).height();
      var elemTop = $(elem).offset().top;
      var elemBottom = elemTop + $(window).height() * 0.5;
      if (elemBottom <= docViewBottom && elemTop >= docViewTop) {
        $(elem).addClass('active');
      }
      if (!(elemBottom <= docViewBottom)) {
        $(elem).removeClass('active');
      }
      var MainTimelineContainer = $('#vertical-scrollable-timeline')[0];
      var MainTimelineContainerBottom = MainTimelineContainer.getBoundingClientRect().bottom - $(window).height() * 0.5;
      $(MainTimelineContainer).find('.inner').css('height', MainTimelineContainerBottom + 'px');
    }
    var timeline = $('#vertical-scrollable-timeline li');
    Array.from(timeline).forEach(isScrollIntoView);
  });

})(window.jQuery);

document.addEventListener("DOMContentLoaded", function () {
  const button = document.getElementById("dropdownUserBtn");
  const menu = document.getElementById("dropdownUserMenu");

  // When the dropdown is shown
  button.addEventListener("click", function () {
    // Wait for Bootstrap to show it
    setTimeout(() => {
      const btnRect = button.getBoundingClientRect();
      const menuRect = menu.getBoundingClientRect();

      // Center the menu under the button
      const offset = (menuRect.width / 2) - (btnRect.width / 2);
      menu.style.left = `${btnRect.left - offset}px`;
      menu.style.top = `${btnRect.bottom + window.scrollY}px`;
      menu.style.position = "absolute";
    }, 10); // Small delay to let Bootstrap render
  });
});

