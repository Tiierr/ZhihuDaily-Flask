var $holders = $('.js-question-holder')
if ($holders.length) {
var list = $holders.map(function(i, el) {
    return $(el).data('aid')
})
$.get('/answer/count', {
    data: list.toArray().toString()
}).done(function(data) {
    $.each(data, function(i, n) {
        $holders.eq(i).text('（' + n + ' 条讨论）')
    })
});
}

var isWechat = false;
if (/micromessenger/.test(navigator.userAgent.toLowerCase())) {
  isWechat = true;
	$('a[href="/download"]').attr('href', 'http://a.app.qq.com/o/simple.jsp?pkgname=com.zhihu.daily.android&g_f=991702');
}
function get_param(name) {
    name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results == null ? "" : results[1].replace(/\+/g, " ");
}
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
})(window,document,'script','//www.google-analytics.com/analytics.js','gq');
gq('create', 'UA-20961733-4', 'zhihu.com');
gq('send', 'pageview');
$('.download a').click(function(){
	gq('send', 'event', 'Topbar', this.dataset.device + 'Download', get_param('utm_source'));
});
$('.header-for-mobile a').click(function(){
    gq('send', 'event', 'Topbar', 'MobileDownload', get_param('utm_source'));
});
$('a.recommend-link').click(function(){
	gq('send', 'event', 'RecommendLink', 'Click', this.dataset.story);
});
$('.bottom-recommend-download-link').click(function(){
    gq('send', 'event', 'BottomBar', 'MobileDownload', get_param('utm_source'));
});

function initWechatShare(imgUrl) {
	var defaultImageURL = "http://static.daily.zhihu.com/img/app-logo.png",
		data = {
			"app": "wx841a6aace4a1dca4",
			"img": imgUrl || defaultImageURL,
			"link": location.href,
			"desc": "分享自@知乎日报",
			"title": document.title
		};
	wechat("friend", data);
	wechat("weibo", data);
	data["img"] = defaultImageURL;
	wechat("timeline", data);
	return true;
}