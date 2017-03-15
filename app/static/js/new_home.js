(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-20961733-4', 'zhihu.com');
ga('send', 'pageview');
var ua = navigator.userAgent.toLowerCase();
if (/iphone|ipad|ipod/.test(ua)) {
	var device = 'iOS';
} else if (/android/.test(ua)) {
	device = 'Android';
} else {
	device = 'Desktop';
}
$('.link-buttons a[data-device]').click(function(){
	ga('send', 'event', 'LP', device + '_Download_' + this.dataset.device);
});