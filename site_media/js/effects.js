// default size
maxWidth = 1280;
maxHeight = 720;

// predefine zIndex value
zIndexer = {"heigh":5, "mid":3, "low":0};

function setSize(){
	// default size
	maxWidth = parseInt(document.getElementById("top_div").style.width);
	maxHeight = parseInt(document.getElementById("top_div").style.height);
}

/**
 * Role: Show an detail article (subject + picture + sentence)
 * Input: 
 	el: current element id (string)
 * Description:
 	1. 현재 Documents의 Name을 바탕으로
	   숨겨진 DIV의 Name을 생성한다.
	2. 숨겨진 DIV를 보여준다.
 # Assumption:
 	숨겨 놓은 DIV의 Id는 보여지는 DIV ID에 detail을 더한 것이다.
 # Additional:
 	Detail DIV를 보여줄 때에 그 위치를 계산 한다.
	(STYLE의 TOP, LEFT 값을 갖고 적당한 위치 계산)
 */
function showDetail(elem){
	// get hidden div elements
	var short_div = elem;
	// get current location
	locTop = parseInt(short_div.style.top);
	locLeft = parseInt(short_div.style.left);
	locWidth = parseInt(short_div.style.width);
	locHeight = parseInt(short_div.style.height);

	// set triangle location and size
	var triangle = document.getElementById('rectangle');
	triangle.width = "30";
	triangle.height = "30";
	triangle.style.top = (((locTop+locHeight/2)>maxHeight/2) ? 
		   locTop-23 : locTop+locHeight+2)+"px";
	triangle.style.left = (locLeft + (locWidth / 2))+"px";
	// show the triangle
	triangle.style.display = 'block';
	triangle.style.zIndex = zIndexer.mid;

	// set detail div location
	var detail_div = document.getElementById(elem.id + '_detail');
	detail_div.style.top = (((locTop+locHeight/2)>maxHeight/2) ? 
			locTop-parseInt(detail_div.style.height)-18 : 
			locTop+locHeight+18) + "px";
	var detailWidth = parseInt(detail_div.style.width);
	detail_div.style.left = (((locLeft+locWidth/2)>maxWidth/2) ? 
			Math.min(maxWidth-detailWidth,locLeft-(detailWidth-locWidth)/2) : 
		   	Math.max(0, locLeft-(detailWidth-locWidth)/2)) + "px";
	// set the element style
	detail_div.style.display = 'block';
	detail_div.style.zIndex = zIndexer.heigh;
}

function hideDetail(elem){
	//get showen div elements
	var detail_div = document.getElementById(elem.id + '_detail');
	detail_div.style.display = 'none';
	detail_div.style.zIndex = zIndexer.low;
	// hide rectangle
	var triangle = document.getElementById('rectangle');
	triangle.style.display = 'none';
	triangle.style.zIndex = zIndexer.low;
}

/**
 * Role: Show an whole article
 * Input:
	link: the linke of the article
 * Description:
 	숨겨져 있는 iFrame에 해당 기사를 담아서 보여준다.
 * Assumption:
 	숨겨 놓은 iFrame이 존재하며, 그 이름은 articleContainer
 */
function showArticle(link){
	// get iFrame object
	var hiddenIframe = document.getElementById('articleContainer');

	// set article
	hiddenIframe.style.display = 'block';
	hiddenIframe.style.zIndex = zIndexer.heigh;
	hiddenIframe.src = link;
}
function hideArticle(){
	// get iFrame object
	var hiddenIframe = document.getElementById('articleContainer');

	// hide article
	hiddenIframe.style.display = 'none';
	hiddenIframe.style.zIndex = zIndexer.low;
	hiddenIframe.src = '';
}

/**
 * iFrame의 크기를 자동으로 조절해 주는 script
 */
function resizeIF() {
	var Id = "articleContainer"
	var obj = document.getElementById(Id);
	var Body;
	var H, Min;

	// 최소 높이 설정 (너무 작아지는 것을 방지)
	Min = 200;

	// DOM 객체 할당
	try
	{
		if (!document.all && obj.contentWindow.document.location.href == 'about:blank') {
			setTimeout("resizeIF('"+Id+"')", 10);
			return;
		}

		Body = obj.contentWindow.document.getElementsByTagName('BODY');
		Body = Body[0];

		if (this.Location != obj.contentWindow.document.location.href) {
			H = Body.scrollHeight + 5;
			obj.style.height =  (H<Min?Min:H) + 'px';

			this.Location = obj.contentWindow.document.location.href;
		}
	}
	catch(e)
	{
		setTimeout("resizeIF('"+Id+"')", 10);
		return;
	}

	setTimeout("resizeIF('"+Id+"')", 100);
}
