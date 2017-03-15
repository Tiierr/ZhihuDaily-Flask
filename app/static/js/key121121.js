// 按钮下拉菜单
function zsAppShow(obj){
	obj.getElementsByTagName("div").item(0).style.display="block";
}
function zsAppHide(obj){
	obj.getElementsByTagName("div").item(0).style.display="none";
}

var Key = new function () {


    //获取url中的指定参数值1
    function getParameter(url, paramName) {
        var re = new RegExp("(^|\\?|&)" + paramName + "=([^&]*)(\s|&|$)", "i");
        if (re.test(url))
            return RegExp.$2;
        else
            return null;
    }

    String.prototype.containDBChar = function () { if (this.match(/[^\x00-\xff]/g) == null) return false; return this.match(/[^\x00-\xff]/g).length > 0; }

    function $id(id) {
        return document.getElementById(id);
    }

    var codeBase = "onekey",
		style = "",
		info = "",
		imgsUrl = "" //图片目录
    previewImgs = [
    "http://zs.91.com/upload/2014/03/17/api/appalpha.png",
    "http://zs.91.com/upload/2014/03/17/api/bg_pop.png",
	"http://zs.91.com/upload/2014/03/17/api/ie6bg_pop.gif",
	"http://zs.91.com/upload/2014/03/17/api/pic1new.gif",
	"http://zs.91.com/upload/2014/03/17/api/pic2new.gif",
    "http://zs.91.com/upload/2014/03/17/api/script.gif"]; //图片名称 （预加载)


    style += "<style type=\"text\/css\">";
    style += "body, div, span, form, input, h1, h2, h3, h4, h6, p, a, em, img, b, dl, dt, dd, ul, li, label{ padding: 0; margin: 0;}";
    style += "input { vertical-align:middle;}";
    style += "input, select { font:12px Tahoma, Geneva, Arial, Helvetica, sans-serif;}";
    style += "img { border: 0; }";
    style += "em { font-style:normal; }";
    style += "ul { list-style: none; }";
    style += "h1, h2, h3, h4, h6 { font-size: 100%; }";
	style += '.clearfix:after{ content:""; height:0; visibility:hidden; display:block; clear:both;}';
	style += '.clearfix{ zoom:1;}';
	style += '.onekey_preview { position: absolute; width: 0px; height: 0px; overflow: hidden; left: 0; top: 0; }';
	style += '.onekey_bg { position: absolute; left: 0; top: 0; background-color: #000; opacity: 0.6; filter: alpha(opacity=60); width: 100%; height: 1px; display: none; z-index: 10000; }';
	style += 'a {color: #39442e; text-decoration:none; outline:none;}';
	style += 'a:hover {text-decoration:underline;}';
	style += '.onekey_con{ display:none; background:url(http://zs.91.com/upload/2014/03/17/api/bg_pop.png) no-repeat; padding:15px; width:570px; height:397px; z-index:99999; position: fixed; _position: absolute; top: 24%; left: 50%; margin-left: -285px; _top:expression(documentElement.scrollTop+0.76*documentElement.clientHeight-this.offsetHeight)}';
	style += '.poptitle{ height:37px; padding:0 0 0 12px; position:relative; zoom:1;}';
	style += '.poptitle .logo{ display:block; float:left; width:24px; height:37px; background:url(http://zs.91.com/upload/2014/03/17/api/script.gif) no-repeat 0 0; margin:0 6px 0 0;}';
	style += '.poptitle span.s1{ display:inline-block; float:left; height:37px; line-height:37px; font-size:14px; color:#999999; font-weight:normal;}';
	style += '.poptitle .close_btn{ display:block; width:13px; height:13px; position:absolute; top:13px; right:14px; background:url(http://zs.91.com/upload/2014/03/17/api/script.gif) no-repeat -25px 0; overflow:hidden;}';
	style += '.poptitle .close_btn:hover{ background-position:-25px -14px;}';
	style += '.pop_con1{ height:65px; padding:17px 0 18px 42px;}';
	style += '.pop_con1 .appcon{ display:block; width:65px; height:65px; position:relative; float:left; overflow:hidden; margin:0 14px 0 0;}';
	style += '.pop_con1 .appcon img{ display:block; width:65px; height:65px;}';
	style += '.pop_con1 .appcon span.r_border65{ display:block; width:65px; height:65px; position:absolute; top:0; left:0; background:url(http://zs.91.com/upload/2014/03/17/api/appalpha.png) no-repeat;}';
	style += '.pop_con1 .app_tiptxt{ display:inline-block; height:65px; line-height:65px; font-size:22px; color:#333333;}';
	style += '.pop_con2{ height:154px; background:#f4f4f4; padding:26px 0 0 41px; position:relative; zoom:1; _margin:0 1px;}';
	style += '.pop_con2 p.p1{ height:50px; line-height:50px; font-family:"宋体"; font-size:16px; color:#666666; font-weight:bold;}';
	style += '.pop_con2 p.p2{ font-size:14px; color:#666666; font-family:"宋体"; line-height:28px;}';
	style += '.pop_con2 .rightpic{ display:block; width:176px; height:166px; background:url(http://zs.91.com/upload/2014/03/17/api/pic1new.gif) no-repeat; position:absolute; top:7px; right:27px;}';
	style += '.pop_con3{ padding:19px 42px 0 0;}';
	style += '.pop_con3 a{ display:block; width:110px; height:39px; float:right; margin:0 0 0 16px; line-height:39px; text-align:center; font-size:16px; background:url(http://zs.91.com/upload/2014/03/17/api/script.gif) no-repeat;}';
	style += '.pop_con3 a.grey_btn{ background-position:0 -118px; color:#666666;}';
	style += '.pop_con3 a.grey_btn:hover{ background-position:0 -158px; text-decoration:none;  color:#FFFFFF;}';
	style += '.pop_con3 a.blue_btn{ background-position:0 -38px; color:#fff;}';
	style += '.pop_con3 a.blue_btn:hover{ background-position:0 -78px; text-decoration:none;}';
	style += '.pop_con_2{ height:230px; background:#f4f4f4; padding:0 0 0 40px; _margin:0 1px;}';
	style += '.pop_con_2 p.p1{ height:44px; line-height:44px; font-size:12px; font-family:"宋体"; color:#666666;}';
	style += '.pop_con_2 img{ margin:8px 0 0 0;}';
	style += '.pop_con_2 p.p2{ height:38px; line-height:38px; font-size:12px; font-family:"宋体"; color:#666666;}';
	style += '.pop_con_2 p.p2 a{ color:#3399cc; padding:0 7px;}';
	style += '.pop_con_3{ height:30px; line-height:30px; _line-height:25px; padding:0 19px 0 0; font-size:12px; font-family:"宋体"; color:#666666; text-align:right;}';
	style += '.pop_con_3 em{ padding:0 7px; color:#ef4300;}';
    style += '.zsDoubleApp{ position:relative; display:inline-block; z-index:9999;}';
	style += '.zsDoubleApp img{ position:relative; z-index:10;}';
	style += '.zsDoubleApp .list{ position:absolute;  padding:0 4px; display:none;}';
	style += '.zsDoubleApp .list a{ display:block; text-align:center; text-decoration:none;}';
	style += '.zsDoubleApp .list a:hover{ background:#000;}';
	style += '.zsDoubleApp_white_b .list a:hover,.zsDoubleApp_white_m .list a:hover,.zsDoubleApp_white_s .list a:hover{background:#bebebe;}';
	style += '.zsDoubleApp_black_b .list a,.zsDoubleApp_black_m .list a,.zsDoubleApp_black_s .list a{color:#fff; background:#292729;}';
	style += '.zsDoubleApp_white_b .list a,.zsDoubleApp_white_m .list a,.zsDoubleApp_white_s .list a{color:#565656; background:#fff; font-weight:bold;}';
	style += '.zsDoubleApp_black_b,.zsDoubleApp_white_b{ width:390px; height:140px; }';
	style += '.zsDoubleApp_black_b .list,.zsDoubleApp_white_b .list{width:375px; left:2px; top:130px;}';
	style += '.zsDoubleApp_black_b .list a,.zsDoubleApp_white_b .list a{ height:40px; line-height:40px;}';
	style += '.zsDoubleApp_black_m,.zsDoubleApp_white_m{ width:280px; height:100px;}';
	style += '.zsDoubleApp_black_m .list,.zsDoubleApp_white_m .list{width:265px;top:86px;left:0px;}';
	style += '.zsDoubleApp_black_m .list a,.zsDoubleApp_white_m .list a{ height:35px; line-height:35px;}';
	style += '.zsDoubleApp_black_s,.zsDoubleApp_white_s{ width:210px; height:77px;}';
	style += '.zsDoubleApp_black_s .list,.zsDoubleApp_white_s .list{width:197px; top:70px; left:0px;}';
	style += '.zsDoubleApp_black_s .list a,.zsDoubleApp_white_s .list a{ height:30px; line-height:30px;}';
    style += "<\/style>";










    //先加载背景图片，不显示
    for (var i = 0; i < previewImgs.length; i++) {
        info += "<div class=\"onekey_preview\"><img src=\"" + imgsUrl + previewImgs[i] + "\" alt=\"\" \/><\/div>";
    }
    info += "<div class=\"onekey_bg\" id=\"onekey_float_bg\"></div>";
    info += "<div class=\"onekey_con\" id=\"onekey_float_con\"></div>";


    document.write(style + info);
    var bg = document.getElementById("onekey_float_bg");
    var con = document.getElementById("onekey_float_con");
    //关闭窗口
    var globalTime = 15;
    var globalTimeId;

    function setCookie(sName, sValue, oExpires, sPaht, sDomain, bSecure) {
        var sCookie = sName + "=" + encodeURIComponent(sValue);
        if (oExpires) {
            sCookie += "; expires=" + oExpires.toGMTString();
        }
        if (sPaht) {
            sCookie += "; path=" + sPaht;
        }
        if (sDomain) {
            sCookie += "; domain=" + sDomain;
        }
        if (bSecure) {
            sCookie += "; secure";
        }
        document.cookie = sCookie;
    }

    function getCookie(sName) {
        var sRE = "(?:; )?" + sName + "=([^;]*);?";
        var oRE = new RegExp(sRE);
        if (oRE.test(document.cookie)) {
            return decodeURIComponent(RegExp["$1"]);
        } else {
            return null;
        }
    }


    function closeWindows() {
        $id("onekey_float_bg").style.display = "none";
        $id("onekey_float_con").style.display = "none";
        $id("onekey_float_con").innerHTML = "";
        globalTime = 15;
        clearInterval(globalTimeId);
    }

    function autoClose() {
        document.getElementById("times").innerHTML = globalTime--;
        if (globalTime == -1) {
            globalTime = 15;
            clearInterval(globalTimeId);
            closeWindows();
        }
    }

    function SetDisplay() {
        $id("onekey_float_con").style.display = "block";
        $id("onekey_float_bg").style.height = (document.documentElement.scrollHeight > document.documentElement.clientHeight) ? document.documentElement.scrollHeight + "px" : document.documentElement.clientHeight + "px";
        $id("onekey_float_bg").style.display = "block";
        var sCookie = getCookie("onekey");
        if (sCookie) {
            globalTimeId = setInterval(autoClose, 1000);
        }
    }
    function checkUrl(url) {
        try {
            setTimeout(function () { location = url; }, 100);
        } catch (err) { }
    }

    this.hidePopup = function () {
        $id("onekey_float_bg").style.display = "none";
        $id("onekey_float_con").style.display = "none";
        $id("onekey_float_con").innerHTML = "";
        globalTime = 15;
        clearInterval(globalTimeId);
    }
    function showPopup() {
        $id("onekey_float_bg").style.display = "block";
        $id("onekey_float_con").style.display = "block";
    }
    this._fnSetCookie = function () {
       var cdate = new Date();
		 cdate.setMinutes(cdate.getMinutes() + 1);
		 if(cdate.getMinutes()>59){
			 cdate.setMinutes(0);
			 cdate.setHours(cdate.getHours()+1)
		 }
        setCookie("onekey", "1", cdate);
        Key.Open(Key.objThis, Key.platformThis);
    };
    this.objThis = "";
    this.platformThis = "";
    this.downloadurlThis = "";
    this.actionTypeThis = "";

    this.urlThis = "";
    this.softIcon = "http://zs.91.com/upload/images/api/v3/icon.jpg";
    this._fnReload = function () {
        checkUrl("mobile91://" + this.urlThis);
    };
    function GetWin(obj, platform, downloadurl, url) {
        var simg = obj.attributes["SoftIcon"];
        if (simg) {
            Key.softIcon = simg.value;
        }
        //        Key.objThis = obj;
        //        Key.platformThis = platform;
        Key.downloadurlThis = downloadurl;
        Key.urlThis = url;
        var win1 = "", win2 = "";
        win1 += '<div class="popcon" id="onekey_win_null">';
			win1 += '<div class="poptitle clearfix">';
			win1 += '<span class="logo"></span>';
			win1 += '<span class="s1">91助手</span>';
			win1 += '<a href="javascript:;" class="close_btn" onClick="Key.hidePopup();"></a>';
			win1 += '</div>';
			win1 += '<div class="pop_container">';
			win1 += '<div class="pop_con1 clearfix">';
			win1 += '<div class="appcon"><span class="r_border65"></span><img src="'+Key.softIcon+'" /></div>';
			win1 += '<span class="app_tiptxt">正在启动一键安装...</span>';
			win1 += '</div>';
			win1 += '<div class="pop_con2">';
			win1 += '<p class="p1">您安装91助手了吗？</p>';
			win1 += '<p class="p2">使用一键安装功能，需先安装91助手<br />91助手将自动安装应用到您的设备</p>';
			win1 += '<span class="rightpic"></span>';
			win1 += '</div>';
			win1 += '<div class="pop_con3 clearfix">';
			win1 += '<a href="javascript:;" class="grey_btn" onClick="Key._fnSetCookie();">我已安装</a>';
			win1 += '<a href="'+downloadurl+'" class="blue_btn">下载91助手</a>';
			win1 += '</div>';
			win1 += '</div>';
			win1 += '</div>';
			
			win2 += '<div class="popcon" id="onekey_win">';
			win2 += '<div class="poptitle clearfix">';
			win2 += '<span class="logo"></span>';
			win2 += '<span class="s1">91助手</span>';
			win2 += '<a href="javascript:;" class="close_btn" onclick="Key.hidePopup();"></a>';
			win2 += '</div>';
			win2 += '<div class="pop_container">';
			win2 += '<div class="pop_con1 clearfix">';
			win2 += '<div class="appcon clearfix"><span class="r_border65"></span><img src="'+Key.softIcon+'" /></div>';
			win2 += '<span class="app_tiptxt">正在打开91助手为您安装应用，请稍候...</span>';
			win2 += '</div>';
			win2 += '<div class="pop_con_2">';
			win2 += '<img src="http://zs.91.com/upload/2014/03/17/api/pic2new.gif" />';
			win2 += '<p class="p2">如果91助手没有打开，请<a href="javascript:;" onclick="Key._fnReload();">重试</a> ；如果您未安装91助手，请<a href="'+downloadurl+'">下载安装</a></p>';
			win2 += '</div>';
			win2 += '<p class="pop_con_3">本窗口将在<em id="times"></em>秒后自动关闭</p>';
			win2 += '</div>';
			win2 += '</div>';


        var sCookie = getCookie("onekey");
        if (sCookie) {
            return win2;
        }
        else {
            return win1;
        }
		return win1;
    }

    $id("onekey_float_bg").onclick = closeWindows;
    this.Open = function (obj, platform, actionType) {
        if (obj && obj.tagName && obj.tagName.toLowerCase() == "a") {
            if (!obj.href) { alert("您的应用下载地址没有填写，请在A标签的href中输入您的应用下载地址"); return false; }
            if (!obj.name) { alert("您的应用中文名称没有填写，请在A标签的name中输入您的应用中文名称"); return false; }
            Key.objThis = obj;
            Key.platformThis = platform;
            Key.actionTypeThis = actionType;
            this.getJson("scrAssistantLatest", "http://zs.91.com/script/api/1key.shtml");
            this.getJson("scrOneKey", "http://zy.91.com/Services/OneKeyInstall.aspx?downurl=" + encodeURIComponent(obj.href) + "&platform=" + platform);
            return false;
        }
    };

    this.checkUrl = function (url) {
        checkUrl(url);
    }

    this.getJson = function (sid, url) {
        var scriptTag = document.getElementById(sid);
        var oHead = document.getElementsByTagName('HEAD').item(0);
        var oScript = document.createElement("script");

        if (scriptTag) {
            oHead.removeChild(scriptTag);
        }
        oScript.id = sid;
        oScript.language = "javascript";
        oScript.type = "text/javascript";
        oScript.src = url;
        oHead.appendChild(oScript);
    }

    this.callBack = function (data) {
        var obj = Key.objThis;
        var platform = Key.platformThis;
        var downloadurl = Key.downloadurlThis;
        var actionType = Key.actionTypeThis;

        var url = obj.href.replace(/^\S*?:\/\//gi, "");
        var fname = getParameter(obj.href, "f_name");
        var aname = obj.name;
        if (obj.name != "" && aname.containDBChar()) {
            url = url.replace("f_name=" + fname, "f_name=" + escape(aname));
        }
        else {
            if (fname.containDBChar()) {
                url = url.replace("f_name=" + fname, "f_name=" + escape(fname));
            }
        }





        if (data) {
            url += "&did=" + data.resId + "&position=" + data.posId;
        }


        if (actionType && actionType == 1) { //客户端已装91助手
            checkUrl("mobile91://" + url);
            return false;
        }

        showPopup();
        SetDisplay();

		var downUrl = "http://dl.ops.baidu.com/91zhushoupc_Windows_1011080h.exe";
        //try {
//            if (assistantLatestUrl) {
//                downUrl = assistantLatestUrl;
//            }
//        } catch (e) {
//
//        }

        if (obj.attributes["downloadurl"]) {

            downUrl = obj.attributes["downloadurl"].value;
        }
        var sWin = GetWin(obj, platform, downUrl, url);
        $id("onekey_float_con").innerHTML = sWin;

        var sCookie = getCookie("onekey");
        if (sCookie) {
            checkUrl("mobile91://" + url);
        }
    }
};