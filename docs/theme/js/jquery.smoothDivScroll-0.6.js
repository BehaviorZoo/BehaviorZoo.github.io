/**
* jQuery.smoothDivScroll - Smooth div scrolling using jQuery.
* This plugin is for turning a set of DIV's into a smooth scrolling area.
*
* Copyright (c) 2009 Thomas Kahn - thomas.kahn(at)karnhuset(dot)net
*
* This plugin is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* any later version.
*
* This plugin is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details. <http://www.gnu.org/licenses/>.
*
* Date: 2009-03-05
* @author Thomas Kahn
* @version 0.6
*
*/

(function($) { 
	jQuery.fn.smoothDivScroll = function(options){

		var defaults = {
		scrollingHotSpotLeft: "div.scrollingHotSpotLeft", // The hotspot that triggers scrolling left
		scrollingHotSpotRight: "div.scrollingHotSpotRight", // The hotspot that triggers scrolling right
		scrollWrapper: "div.scrollWrapper", // The wrapper element that surrounds the scrollable area
		scrollableArea: "div.scrollableArea", // The actual element that is scrolled left or right
		hiddenOnStart: false, // True or false. Determines whether the element should be visible or hidden
		ajaxContentURL: "", // Optional. If supplied, content is fetched through AJAX using the supplied URL
		countOnlyClass: "", // Optional. If supplied, the function that calculates the width of the scrollable area will only count elements of this class
		mouseDownSpeedBooster: 1 // 1 is normal speed, 2 is twice as fast, 3 is three times as fast, and so on
		};

		options = $.extend(defaults, options);

		// Iterate and reformat each matched element
		return this.each(function() {
		
			// Create a variable for the current "mother element"
			var $mom = $(this);
			
			// Load the content of the scrollable area using the optional URL.
			// If no ajaxContentURL is supplied, we assume that the content of
			// the scrolling area is already in place.
			if(options.ajaxContentURL.length !== 0){
				$mom.scrollableAreaWidth = 0;
				$mom.find(options.scrollableArea).load((options.ajaxContentURL), function(){	
					$mom.find(options.scrollableArea).children((options.countOnlyClass)).each(function() {
						$mom.scrollableAreaWidth = $mom.scrollableAreaWidth + $(this).outerWidth(true);
					});

					// Set the width of the scrollable area
					$mom.find(options.scrollableArea).css("width", ($mom.scrollableAreaWidth + "px"));
					
					// Hide the mother element if it shouldn't be visible on start
					if(options.hiddenOnStart) {
						$mom.hide();
					}
					
					windowIsResized();
					
					setHotSpotHeightForIE();
				});		
			}
				
			// The left offset of the container on which you place 
			// the scrolling behavior.
			// This offset is used when calculating the mouse x-position 
			// in relation to scroll hotspots
			var motherElementOffset = $mom.offset().left;
			
			// A variable used for storing the current hotspot width.
			// It is used when calculating the scroll speed
			var hotSpotWidth = 0;
			
			// Set the booster value to normal (doesn't change until the user
			// holds down the mouse button over one of the hotspots)
			var booster = 1;
			
			// If the content of the scrolling area is not loaded through ajax,
			// we assume it's already there and can run the code to calculate
			// the width of the scrolling area, resize it to that width
			$(window).one("load",function(){
				if(options.ajaxContentURL.length === 0) {
					$mom.scrollableAreaWidth = 0;
					$mom.find(options.scrollableArea).children((options.countOnlyClass)).each(function() {
						$mom.scrollableAreaWidth = $mom.scrollableAreaWidth + $(this).outerWidth(true);
					});
					
					$mom.find(options.scrollableArea).css("width", $mom.scrollableAreaWidth + "px");
					
					if(options.hiddenOnStart) { 
						$mom.hide();
					}
				}
			});
			
			// EVENT - window resize
			$(window).bind("resize",function(){
				windowIsResized();
			});

			// A function for doing the stuff that needs to be
			// done when the browser window is resized
			function windowIsResized()
			{
				// If the scrollable area is not hidden on start, reset and recalculate the
				// width of the scrollable area
				if(!(options.hiddenOnStart))
				{
					$mom.scrollableAreaWidth = 0;
					$mom.find(options.scrollableArea).children((options.countOnlyClass)).each(function() {
						$mom.scrollableAreaWidth = $mom.scrollableAreaWidth + $(this).outerWidth(true);
					});
					
					$mom.find(options.scrollableArea).css("width", $mom.scrollableAreaWidth + 'px');
				}

				// Reset the left offset of the scroll wrapper
				$mom.find(options.scrollWrapper).scrollLeft("0");
				
				// Get the width of the page (body)
				var bodyWidth = $("body").innerWidth();
				
				// If the scrollable area is shorter than the current
				// window width, both scroll hotspots should be hidden.
				// Otherwise, check which hotspots should be shown.
				if($mom.scrollableAreaWidth < bodyWidth)
				{	
					hideLeftHotSpot();
					hideRightHotSpot();
				}
				else
				{
					showHideHotSpots();
				}
			}
			
			// HELPER FUNCTIONS FOR SHOWING AND HIDING HOT SPOTS
			function hideLeftHotSpot(){
				$mom.find(options.scrollingHotSpotLeft).hide();
			}
			
			function hideRightHotSpot(){
				$mom.find(options.scrollingHotSpotRight).hide();
			}
			
			function showLeftHotSpot(){
				$mom.find(options.scrollingHotSpotLeft).show();
				// Recalculate the hotspot width. Do it here because you can
				// be sure that the hotspot is visible and has a width
				if(hotSpotWidth <= 0)
				{
				hotSpotWidth = $mom.find(options.scrollingHotSpotLeft).width();
				}
			}
			
			function showRightHotSpot(){
				$mom.find(options.scrollingHotSpotRight).show();
				// Recalculate the hotspot width. Do it here because you can
				// be sure that the hotspot is visible and has a width
				if(hotSpotWidth <= 0)
				{
				hotSpotWidth = $mom.find(options.scrollingHotSpotRight).width();
				}
			}
			
			function setHotSpotHeightForIE()
			{
				jQuery.each(jQuery.browser, function(i, val) {
					if(i=="msie" && jQuery.browser.version.substr(0,1)=="6")
					{
						$mom.find(options.scrollingHotSpotLeft).css("height", ($mom.find(options.scrollableArea).innerHeight()));
						$mom.find(options.scrollingHotSpotRight).css("height", ($mom.find(options.scrollableArea).innerHeight()));						
					}
				});
			}
			
			// EVENTS - scroll right
			var rightScrollInterval;
			var scrollXpos;

			
			$mom.find(options.scrollingHotSpotRight).bind('mousemove',function(e){
				var x = e.pageX - (this.offsetLeft + motherElementOffset);
				x = Math.round(x/(hotSpotWidth/15));
				scrollXpos = x;
				
			});

			$mom.find(options.scrollingHotSpotRight).bind('mouseover',function(e){
				rightScrollInterval = setInterval(doScrollRight, 15);
			});	

			$mom.find(options.scrollingHotSpotRight).bind('mouseout',function(e){
				clearInterval(rightScrollInterval);
				scrollXpos = 0;
			});
			
			// scrolling speed booster right
			$mom.find(options.scrollingHotSpotRight).bind('mousedown',function(e){
				booster = options.mouseDownSpeedBooster;
			});
			
			// stop boosting the scrolling speed
			$("*").bind('mouseup',function(e){
				booster = 1;
			});
			
			// The function that does the actual scrolling right
			var doScrollRight = function()
			{	
				$mom.find(options.scrollWrapper).scrollLeft($mom.find(options.scrollWrapper).scrollLeft() + (scrollXpos*booster));
				showHideHotSpots();
			};
			
			// EVENTS - scroll left
			var leftScrollInterval;
			
			// mousemove left hotspot
			$mom.find(options.scrollingHotSpotLeft).bind('mousemove',function(e){
				var x = $mom.find(options.scrollingHotSpotLeft).innerWidth() - (e.pageX - motherElementOffset);
				x = Math.round(x/(hotSpotWidth/15));
				scrollXpos = x;
			});
			
			// mouseover left hotspot
			$mom.find(options.scrollingHotSpotLeft).bind('mouseover',function(e){
				leftScrollInterval = setInterval(doScrollLeft, 15);
			});	
			
			// mouseout left hotspot
			$mom.find(options.scrollingHotSpotLeft).bind('mouseout',function(e){
				clearInterval(leftScrollInterval);
				scrollXpos = 0;
			});
			
			// scrolling speed booster left
			$mom.find(options.scrollingHotSpotLeft).bind('mousedown',function(e){
				booster = options.mouseDownSpeedBooster;
			});
			
			// The function that does the actual scrolling left
			var doScrollLeft = function()
			{	
				$mom.find(options.scrollWrapper).scrollLeft($mom.find(options.scrollWrapper).scrollLeft() - (scrollXpos*booster));
				showHideHotSpots();			
			};
			
			// Function for showing and hiding hotspots depending on the
			// offset of the scrolling
			function showHideHotSpots()
			{
				// When you can't scroll further left
				// the left scroll hotspot should be hidden
				// and the right hotspot visible
				if($mom.find(options.scrollWrapper).scrollLeft() === 0)
				{
					hideLeftHotSpot();
					showRightHotSpot();
				}
				// When you can't scroll further right
				// the right scroll hotspot should be hidden
				// and the left hotspot visible
				else if(($mom.scrollableAreaWidth) <= ($mom.find(options.scrollWrapper).innerWidth() + $mom.find(options.scrollWrapper).scrollLeft()))
				{
					hideRightHotSpot();
					showLeftHotSpot();
				}
				// If you are somewhere in the middle of your
				// scrolling, both hotspots should be visible
				else
				{
					showRightHotSpot();
					showLeftHotSpot();
				}

			}
	});
};

})(jQuery);

