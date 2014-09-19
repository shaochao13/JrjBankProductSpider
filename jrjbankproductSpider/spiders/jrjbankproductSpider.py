# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
import json


class JrjBankProductSpider(BaseSpider):
    allowed_domains = ["bank.jrj.com.cn"]
    start_urls = [u'http://bank.jrj.com.cn/action/bankproduct.jspa?page=1&order=SELL_END_DATE%20desc&bankid=0&cur=0&yield=0&sell=0&productname=&period=0&yieldtype=&holding=&atone=&beginDate=&endDate=&wf=1']
    name = 'jrjBankProductSpider'


    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        pageIndex = jsonresponse["page"]
        productsum = jsonresponse["pagesum"]
        products = jsonresponse["product"]

        for item in products:
            productID = item['productID']
            productName = item['productName']
            stopCond = item['stopCond']
            term = item['term']
            termType = item['termType']
            venture = item['venture']
            yield_Value = item['yield']
            yieldType = item['yieldType']
            yielddate = item['yielddate']
            yieldExplain = item['yieldExplain']
            addr = item["addr"]
            atoneBank = item['atoneBank']
            atoneCustormer = item['atoneCustormer']
            bankID = item['bankID']
            bankName = item['bankName']
            beginDate = item['beginDate']
            endDate = item['endDate']
            beginMoney = item['beginMoney']
            buyCond = item['buyCond']
            cur = item['cur']
            curncyType = item['curncyType']
            dp = item['dp']
            feature = item['feature']
            holding = item['holding']
            interestTerm = item['interestTerm']
            isQDII = item['isQDII']
            jf = item['jf']
            manageFee = item['manageFee']
            moneyUnit = item['moneyUnit']
            print(bankName)



# var wf = "";
# function InitBankSel(id, val) {
# 	var banksel = $(id);
# 	banksel.length = 0;
# 	banksel.options[banksel.length] = new Option("银行", "0");
# 	for (i = 0; i < bank.length; i++) {
# 		banksel.options[banksel.length] = new Option(bank[i][1], bank[i][0]);
# 		if (bank[i][0] == val)
# 			banksel.options[banksel.length - 1].selected = true;
# 	}
# }
# function InitBZSel(id, val) {
# 	var bzsel = $(id);
# 	bzsel.length = 0;
# 	bzsel.options[bzsel.length] = new Option("委托币种", "0");
# 	for (i = 0; i < currency.length; i++) {
# 		bzsel.options[bzsel.length] = new Option(currency[i][1], currency[i][0]);
# 		if (currency[i][0] == val)
# 			bzsel.options[bzsel.length - 1].selected = true;
# 	}
# }
# function InitYield(id, val) {
# 	var yieldSel = $(id);
# 	yieldSel.length = 0;
# 	yieldSel.options[yieldSel.length] = new Option("预期收益", "0");
# 	yieldSel.options[yieldSel.length] = new Option("3%以下", "1");
# 	yieldSel.options[yieldSel.length] = new Option("3%---5%", "2");
# 	yieldSel.options[yieldSel.length] = new Option("5%--10%", "3");
# 	yieldSel.options[yieldSel.length] = new Option("10%---15%", "4");
# 	yieldSel.options[yieldSel.length] = new Option("15%--20%", "5");
# 	yieldSel.options[yieldSel.length] = new Option("20%以上", "6");
# 	yieldSel.options[val].selected = true;
# }
# function InitSell(id, init, val) {
# 	var sellSel = $(id);
# 	sellSel.length = 0;
# 	sellSel.options[sellSel.length] = new Option(init, "0");
# 	sellSel.options[sellSel.length] = new Option("是", "1");
# 	sellSel.options[sellSel.length] = new Option("否", "2");
# 	sellSel.options[val].selected = true;
# }
# function InitPeriod(id, val) {
# 	var periodSel = $(id);
# 	periodSel.length = 0;
# 	periodSel.options[periodSel.length] = new Option("委托期限", "0");
# 	periodSel.options[periodSel.length] = new Option("3个月以下", "1");
# 	periodSel.options[periodSel.length] = new Option("3-6个月", "2");
# 	periodSel.options[periodSel.length] = new Option("6-12个月", "3");
# 	periodSel.options[periodSel.length] = new Option("13-24个月", "4");
# 	periodSel.options[periodSel.length] = new Option("24个月以上", "5");
# 	periodSel.options[val].selected = true;
# }
# function InitYieldType(id, val) {
# 	var yieldtypeSel = $(id);
# 	yieldtypeSel.length = 0;
# 	yieldtypeSel.options[yieldtypeSel.length] = new Option("收益类型", "0");
# 	yieldtypeSel.options[yieldtypeSel.length] = new Option("浮动收益", "1");
# 	yieldtypeSel.options[yieldtypeSel.length] = new Option("固定收益", "2");
# 	yieldtypeSel.options[val].selected = true;
# }
# function InitBeginMoney(id, val) {
# 	var bmoneydSel = $(id);
# 	bmoneydSel.length = 0;
# 	bmoneydSel.options[bmoneydSel.length] = new Option("委托起始金额", "0");
# 	bmoneydSel.options[bmoneydSel.length] = new Option("低于1千元", "1");
# 	bmoneydSel.options[bmoneydSel.length] = new Option("1千元-1万元", "2");
# 	bmoneydSel.options[bmoneydSel.length] = new Option("1万元-10万元", "3");
# 	bmoneydSel.options[bmoneydSel.length] = new Option("10万元以上", "4");
# 	bmoneydSel.options[val].selected = true;
# }
# function SearchProduct(page, sort) {
# 	var content = $("ct");
# 	while (content.firstChild) {
# 		content.removeChild(content.firstChild);
# 	}
# 	var newtr = document.createElement("tr");
# 	var newtd = document.createElement("td");
# 	newtd.colSpan = 12;
# 	newtd.height = "30px";
# 	newtd.className = "check";
# 	newtd.innerHTML = "<img src=\"http:\/\/i0.jrj.com.cn\/fund\/nv\/loading.gif\" border=\"0\" width=\"15\" height=\"15\" style=\"vertical-align: middle\" \/> 数据载入中......<\/td>";
# 	newtr.appendChild(newtd);
# 	content.appendChild(newtr);
# 	var ot1 = $("con_t31_1");
# 	var ot2 = $("con_t31_2");
# 	var banksel = "";
# 	var bzsel = "";
# 	var yieldSel = "";
# 	var sellSel = "";
# 	var productname = "";
# 	var peirod = "";
# 	var yieldtype = "";
# 	var bb = "";
# 	var sh = "";
# 	var begindate = "";
# 	var enddate = "";
# 	var beginMoney = "";
# 	var wf = $("wf").value;
# 	if (ot1.style.display != "none") {
# 		banksel = $("selbank").value;
# 		bzsel = $("selbz").value;
# 		yieldSel = $("selsy").value;
# 		sellSel = $("selsell").value;
# 		beginMoney = $("selqsje").value;
# 		productname = $("txtProductName").value;
# 		peirod = $("selperiod").value;
# 		wf = $("wf1").value;
# 	}
# 	if (ot2.style.display != "none") {
# 		banksel = $("selbank2").value;
# 		bzsel = $("selbz2").value;
# 		yieldSel = $("selsy2").value;
# 		sellSel = $("selsell2").value;
# 		productname = $("txtProductName2").value;
# 		peirod = $("selperiod").value;
# 		yieldtype = $("selyieldtype").value;
# 		bb = $("selbb").value;
# 		sh = $("selsh").value;
# 		beginMoney = $("selqsje2").value;
# 		begindate = $("txtBeginDate").value;
# 		enddate = $("txtEndDate").value;
# 		wf = $("wf2").value;
# 		if (begindate == "始销日")
# 			begindate = "";
# 		if (enddate == "停销日")
# 			enddate = "";
# 	}
# 	var url = '/action/bankproduct.jspa';
# 	if (productname == "输入产品名称")
# 		productname = "";
# 	productname = encodeURI(encodeURI(productname));
# 	bzsel = encodeURI(encodeURI(bzsel));
# 	var params = 'page=' + page + '&order=' + sort + '&bankid=' + banksel
# 			+ "&cur=" + bzsel + "&yield=" + yieldSel + "&sell=" + sellSel
# 			+ "&productname=" + productname + "&period=" + peirod
# 			+ "&yieldtype=" + yieldtype + "&holding=" + bb + "&atone=" + sh
# 			+ "&beginDate=" + begindate + "&endDate=" + enddate + "&wf=" + wf;
# 	new Ajax.Request(url, {
# 		method : 'post',
# 		parameters : params,
# 		onSuccess : getProductJson
# 	});
# }
# function InitLendingType(id, val) {
# 	var ltsel = $(id);
# 	ltsel.length = 0;
# 	ltsel.options[ltsel.length] = new Option("贷款币种", "");
# 	for (i = 0; i < lendingtype.length; i++) {
# 		ltsel.options[ltsel.length] = new Option(lendingtype[i][1],
# 				lendingtype[i][0]);
# 		if (lendingtype[i][0] == val)
# 			ltsel.options[ltsel.length - 1].selected = true;
# 	}
# }
# function getProductJson(request) {
# 	var action = request.responseJSON;
# 	MakeTable(action.product, action.wf);
# 	pager(action.pagesum, action.page, action.order);
# }
# function sort(id) {
# 	var s = "";
# 	var cn = $(id).className;
# 	var obj = $(id).parentNode;
# 	var ths = obj.getElementsByTagName('th');
# 	for (i = 0; i < ths.length; i++) {
# 		if (ths[i].className == 'dbt' || ths[i].className == 'ubt') {
# 			ths[i].className = '';
# 		}
# 	}
# 	if (cn == 'dbt') {
# 		$(id).className = 'ubt';
# 		if (id == "ENTR_MNG_TERM") {
# 			s = "ENTR_MNG_UNIT desc,ENTR_MNG_TERM"
# 		} else {
# 			s = id;
# 		}
# 	} else {
# 		$(id).className = 'dbt';
# 		if (id == "ENTR_MNG_TERM") {
# 			s = "ENTR_MNG_UNIT,ENTR_MNG_TERM desc"
# 		} else {
# 			s = id + " desc";
# 		}
# 	}
# 	SearchProduct('1', s);
# }
# function filChar(s) {
# 	var re = /('|"|\s|\\|&nbsp;|&quot;)+/;
# 	return s.gsub(re, "");
# }
# function MakeTable(data, flag) {
# 	var content = $("ct");
# 	while (content.firstChild) {
# 		content.removeChild(content.firstChild);
# 	}
# 	var cp = new HttpCookie("cp_bank");
# 	var cpid = cp.getValue();
# 	if (cpid != null && cpid.length > 0)
# 		var cpArr = cpid.split(",");
# 	for ( var i = 0; i < data.length; i++) {
# 		var newtr = document.createElement("tr");
# 		var newtd1 = document.createElement("td");
# 		newtd1.className = "check";
# 		var checked = "";
# 		if (cpArr != null && cpArr.length > 0) {
# 			for ( var s = 0; s < cpArr.length; s++) {
# 				if (cpArr[s] == data[i].productID) {
# 					checked = " checked";
# 					break;
# 				}
# 			}
# 		}
# 		newtd1.innerHTML = "<input onclick=\"setCompare('" + data[i].productID
# 				+ "','" + filChar(data[i].productName) + "',this)\" id=\"ic_"
# 				+ data[i].productID + "\" type=\"checkbox\" " + checked + " />";
# 		newtr.appendChild(newtd1);
# 		var newtd2 = document.createElement("td");
# 		newtd2.className = "txl";
# 		var str = "";
# 		var productdetail = "bbproduct_";
# 		if (flag == 2)
# 			productdetail = "wbproduct_";
# 		if (flag == 3)
# 			productdetail = "qdproduct_";
# 		$("wf").value = flag;
# 		$("wf1").value = flag;
# 		$("wf2").value = flag;
# 		var beginSellDate = data[i].beginDate;
# 		var endSellDate = data[i].endDate;
# 		var status = getSellStatus(beginSellDate,endSellDate);
# 		str += status;
# 		str += "<a href=\"/txtProduct/" + productdetail + data[i].productID
# 				+ ".shtml\">" + dd(filChar(data[i].productName), 20)
# 				+ "</a>"
# 		newtd2.innerHTML = str;
# 		newtd2.title = data[i].productName;
# 		newtr.appendChild(newtd2);
# 		var newtd3 = document.createElement("td");
# 		if (isHasBankDetail(data[i].bankID))
# 			newtd3.innerHTML = "<a href=\"/txtBank/banknews_" + data[i].bankID
# 					+ ".shtml\">" + data[i].bankName + "</a>";
# 		else
# 			newtd3.innerHTML = data[i].bankName;
# 		newtr.appendChild(newtd3);
# 		var newtd4 = document.createElement("td");
# 		if (data[i].addr == "" || data[i].addr == null)
# 			newtd4.innerHTML = "---";
# 		else
# 			newtd4.innerHTML = data[i].addr;
# 		newtr.appendChild(newtd4);
# 		if (flag > 1) {
# 			var newtdn = document.createElement("td");
# 			newtdn.innerHTML = data[i].cur + "&nbsp;";
# 			newtr.appendChild(newtdn);
# 		}
# 		var newtd5 = document.createElement("td");
# 		var bd = data[i].beginDate;
# 		if (bd == null || bd == "" || bd == "1900-01-01")
# 			newtd5.innerHTML = "---";
# 		else
# 			newtd5.innerHTML = bd;
# 		newtr.appendChild(newtd5);
# 		var newtd6 = document.createElement("td");
# 		var ed = data[i].endDate;
# 		if (ed == null || ed == "" || ed == "1900-01-01")
# 			newtd6.innerHTML = "---";
# 		else
# 			newtd6.innerHTML = ed;
# 		newtr.appendChild(newtd6);
# 		var newtd7 = document.createElement("td");
# 		if (parseInt(data[i].yield) == 0 || isNaN(parseFloat(data[i].yield).toFixed(2)))
# 			newtd7.innerHTML = "---";
# 		else
# 			newtd7.innerHTML = parseFloat(data[i].yield).toFixed(2) + "%";
# 		newtr.appendChild(newtd7);
# 		var newtd8 = document.createElement("td");
# 		if (data[i].term == "" || data[i].term == null) {
# 			newtd8.innerHTML = "---";
# 		} else {
# 			if (data[i].termType == 1) {
# 				newtd8.innerHTML = data[i].term + "月";
# 			} else {
# 				newtd8.innerHTML = data[i].term + "天";
# 			}
# 		}
# 		newtr.appendChild(newtd8);
# 		if (flag < 3) {
# 			var newtd9 = document.createElement("td");
# 			if (data[i].yieldType == null || data[i].yieldType == "")
# 				newtd9.innerHTML = "---"
# 			else
# 				newtd9.innerHTML = data[i].yieldType;
# 			newtr.appendChild(newtd9);
# 		}
# 		var newtd10 = document.createElement("td");
# 		if (parseInt(data[i].beginMoney) == 0) {
# 			newtd10.innerHTML = "---";
# 		} else {
# 			newtd10.innerHTML = data[i].beginMoney;
# 		}
# 		newtr.appendChild(newtd10);
# 		var newtd11 = document.createElement("td");
# 		if (flag < 3) {
# 			var feature = data[i].feature;
# 			if (feature == null) {
# 				feature = "无";
# 			}
# 			newtd11.innerHTML = "<a title='" + feature + "'>特色</a>";
# 		} else {
# 			var venture = data[i].venture;
# 			if (venture == null) {
# 				venture = "无";
# 			}
# 			newtd11.innerHTML = "<a title='" + venture + "'>风险</a>";
# 		}
# 		newtr.appendChild(newtd11);
# 		var newtd12 = document.createElement("td");
# 		newtd12.innerHTML = data[i].jf;
# 		newtr.appendChild(newtd12);
# 		content.appendChild(newtr);
# 	}
# }
# /**
#  * 根据销售开始时间和结束时间 判断产品的销售状态
#  * @param beginSellDate
#  * @param endSellDate
#  * @returns
#  */
# function getSellStatus(bDate,eDate)
# {
#
# 	 var e = JRJ.date.format(new Date(), "yyyyMMdd");
#    var d;
#    var i;
#    d = bDate.replace(/-/g, "");
#    i = eDate.replace(/-/g, "");
#    if (e >= d && e <= i) {
#        str = "【在售】";
#    } else {
#        if (e < d) {
#            str = "【预售】";
#        } else {
#            str = "【停售】";
#        }
#    }
#    return str;
# }
# function pager(num, page, sort) {
# 	var pagesize = 20;
# 	var pagesum = Math.ceil(num / 20)
# 	var pagestr = "";
# 	if (pagesum > 1) {
# 		if (pagesum <= 12) {
# 			for ( var j = 1; j <= pagesum; j++) {
# 				if (j == page) {
# 					pagestr = pagestr + "<a class=\"sel\">" + j + "</a>";
# 				} else {
# 					pagestr = pagestr + "<a href=\"javascript:SearchProduct('"
# 							+ j + "','" + sort + "')\" target=\"_self\">" + j
# 							+ "</a>";
# 				}
# 			}
# 			if (page > 1) {
# 				pagestr = "<a href=\"javascript:SearchProduct('" + (page - 1)
# 						+ "','" + sort
# 						+ "')\" target=\"_self\">&lt;&lt; 上一页</a>" + pagestr;
# 			} else {
# 				pagestr = "<a>&lt;&lt; 上一页</a>" + pagestr;
# 			}
# 			if (page < pagesum) {
# 				pagestr = pagestr + "<a href=\"javascript:SearchProduct('"
# 						+ (page + 1) + "','" + sort
# 						+ "')\" target=\"_self\">下一页 &gt;&gt;</a>";
# 			} else {
# 				pagestr = pagestr + "<a>下一页 &gt;&gt;</a>";
# 			}
# 		} else {
# 			var pagehead = "<a href=\"javascript:SearchProduct('"
# 					+ (page - 1)
# 					+ "','"
# 					+ sort
# 					+ "')\" target=\"_self\">&lt;&lt; 上一页</a><a href=\"javascript:SearchProduct('1','"
# 					+ sort
# 					+ "')\" target=\"_self\">1</a><a href=\"javascript:SearchProduct('2','"
# 					+ sort + "')\" target=\"_self\">2</a>";
# 			var pageend = "<a href=\"javascript:SearchProduct('"
# 					+ (pagesum - 1) + "','" + sort + "')\" target=\"_self\">"
# 					+ (pagesum - 1)
# 					+ "</a><a href=\"javascript:SearchProduct('" + pagesum
# 					+ "','" + sort + "')\" target=\"_self\">" + pagesum
# 					+ "</a><a href=\"javascript:SearchProduct('" + (page + 1)
# 					+ "','" + sort + "')\" target=\"_self\">下一页 &gt;&gt;</a>";
# 			if (page == 1) {
# 				pagehead = "<a>&lt;&lt; 上一页</a><a class=\"sel\">1</a><a href=\"javascript:SearchProduct('2','"
# 						+ sort + "')\" target=\"_self\">2</a>";
# 			}
# 			if (page == 2) {
# 				pagehead = "<a href=\"javascript:SearchProduct('1','"
# 						+ sort
# 						+ "')\" target=\"_self\">&lt;&lt; 上一页</a><a href=\"javascript:SearchProduct('1','"
# 						+ sort
# 						+ "')\" target=\"_self\">1</a><a class=\"sel\">2</a>";
# 			}
# 			if (page == pagesum - 1) {
# 				pageend = "<a class=\"sel\">" + (pagesum - 1)
# 						+ "</a><a href=\"javascript:SearchProduct('" + pagesum
# 						+ "','" + sort + "')\" target=\"_self\">" + pagesum
# 						+ "</a><a href=\"javascript:SearchProduct('" + pagesum
# 						+ "','" + sort
# 						+ "')\" target=\"_self\">下一页 &gt;&gt;</a>";
# 			}
# 			if (page == pagesum) {
# 				pageend = "<a href=\"javascript:SearchProduct('"
# 						+ (pagesum - 1) + "','" + sort
# 						+ "')\" target=\"_self\">" + (pagesum - 1)
# 						+ "</a><a class=\"sel\">" + pagesum
# 						+ "</a><a>下一页 &gt;&gt;</a>";
# 			}
# 			var pagemid = "";
# 			if (page < 10) {
# 				for ( var j = 3; j <= 10; j++) {
# 					if (j == page) {
# 						pagemid = pagemid + "<a class=\"sel\">" + j + "</a>";
# 					} else {
# 						pagemid = pagemid
# 								+ "<a href=\"javascript:SearchProduct('" + j
# 								+ "','" + sort + "')\" target=\"_self\">" + j
# 								+ "</a>";
# 					}
# 				}
# 				pagemid = pagemid + "...";
# 			} else {
# 				if (page > pagesum - 10) {
# 					for ( var j = pagesum - 2; j >= pagesum - 10; j--) {
# 						if (j == page) {
# 							pagemid = "<a class=\"sel\">" + j + "</a>"
# 									+ pagemid;
# 						} else {
# 							pagemid = "<a href=\"javascript:SearchProduct('"
# 									+ j + "','" + sort
# 									+ "')\" target=\"_self\">" + j + "</a>"
# 									+ pagemid;
# 						}
# 					}
# 					pagemid = "..." + pagemid;
# 				} else {
# 					var i = 8;
# 					var ps = page;
# 					var pe = page;
# 					pagemid = "<a class=\"sel\">" + page + "</a>";
# 					do {
# 						ps--;
# 						pe++;
# 						if (pe >= pagesum - 1) {
# 							break;
# 						}
# 						pagemid = "<a href=\"javascript:SearchProduct('" + ps
# 								+ "','" + sort + "')\" target=\"_self\">" + ps
# 								+ "</a>" + pagemid
# 								+ "<a href=\"javascript:SearchProduct('" + pe
# 								+ "','" + sort + "')\" target=\"_self\">" + pe
# 								+ "</a>";
# 						i = i - 2;
# 					} while (i > 0);
# 					pagemid = "..." + pagemid + "...";
# 				}
# 			}
# 			pagestr = pagehead + pagemid + pageend;
# 		}
# 	}
# 	$('page').innerHTML = pagestr;
# }
# function setCompare(productid, productname, obj) {
# 	if (obj.checked) {
# 		var cp = new HttpCookie("cp_bank");
# 		var cpid = cp.getValue();
# 		var op = $("p0");
# 		if (cpid != null && cpid.length > 0) {
# 			var cpArr = cpid.split(",");
# 			if (cpArr.length >= 4) {
# 				alert('您最多只能选择四项产品进行比较！');
# 				obj.checked = false;
# 				return;
# 			} else {
# 				cpid = cpid + "," + productid;
# 				op = $("p" + cpArr.length);
# 			}
# 		} else {
# 			cpid = productid;
# 		}
# 		op.innerHTML = "<a href=\"javascript:delCompare("
# 				+ productid
# 				+ ",'"
# 				+ obj.id
# 				+ "')\" title=\"删除\" class=\"del\" target=\"_self\"><\/a><span title='"
# 				+ productname + "'>" + productname.substr(0, 9) + "</span>";
# 		cp.setValue(cpid);
# 		cp.save();
# 	} else {
# 		delCompare(productid, obj.id);
# 	}
# }
# function delCompare(productid, objid) {
# 	var cp = new HttpCookie("cp_bank");
# 	var cpid = cp.getValue();
# 	if (cpid != null && cpid.length > 0) {
# 		var cpArr = cpid.split(",");
# 		if (cpArr.length == 1) {
# 			cpid = "";
# 			$("p0").innerHTML = "";
# 		} else {
# 			for ( var i = 0; i < cpArr.length; i++) {
# 				if (cpArr[i] == productid)
# 					break;
# 			}
# 			if (i < cpArr.length) {
# 				cpArr.splice(i, 1);
# 				do {
# 					var j = i + 1;
# 					var opn = $("p" + j);
# 					var opi = $("p" + i);
# 					if (opn != null && opn.innerHTML.length > 0) {
# 						opi.innerHTML = opn.innerHTML;
# 					} else {
# 						opi.innerHTML = "";
# 						break;
# 					}
# 					i++;
# 				} while (i < 4);
# 				cpid = cpArr.join(",");
# 			}
# 		}
# 		if (cpid == "")
# 			cp.setExpires(-1);
# 		cp.setValue(cpid);
# 		cp.save();
# 	}
# 	if ($(objid) != null)
# 		$(objid).checked = false;
# }
# function Compare() {
# 	var cp = new HttpCookie("cp_bank");
# 	var cpid = cp.getValue();
# 	if (cpid != null && cpid.length > 0) {
# 		var cpArr = cpid.split(",");
# 		if (cpArr.length > 1) {
# 			var i;
# 			for (i = 0; i < cpArr.length; i++) {
# 				var op = $("pid" + i);
# 				op.value = cpArr[i];
# 			}
# 			for (; i < 4; i++) {
# 				var op = $("pid" + i);
# 				op.value = "0";
# 			}
# 			$("formbj").submit();
# 			return;
# 		}
# 	}
# 	alert('至少要选择两项才能比较');
# 	return;
# }
# function InitCompare(num) {
# 	while ($("tdcb").firstChild) {
# 		$("tdcb").removeChild($("tdcb").firstChild);
# 	}
# 	while ($("tdcp").firstChild) {
# 		$("tdcp").removeChild($("tdcp").firstChild);
# 	}
# 	for ( var i = 0; i < num; i++) {
# 		var bobj = document.createElement("select");
# 		bobj.style.width = 720 / num + "px";
# 		var pobj = document.createElement("select");
# 		pobj.style.width = 720 / num + "px";
# 		bobj.options[bobj.length] = new Option("银行", "0");
# 		for (j = 0; j < bank.length; j++) {
# 			bobj.options[bobj.length] = new Option(bank[j][1], bank[j][0]);
# 		}
# 		if (wf == "1")
# 			pobj.options[pobj.length] = new Option("本币产品", "0");
# 		else if (wf == "2")
# 			pobj.options[pobj.length] = new Option("外币产品", "0");
# 		else if (wf == "3")
# 			pobj.options[pobj.length] = new Option("QDII产品", "0");
# 		else
# 			pobj.options[pobj.length] = new Option("本外币产品", "0");
# 		s = i + 1;
# 		bobj.id = "cbs" + s;
# 		pobj.className = "calssName_nfId";
# 		pobj.name = "id" + s;
# 		pobj.id = "id" + s;
# 		bobj.onchange = function() {
# 			GetProduct(this.value, this.id);
# 		}
# 		$("tdcb").appendChild(bobj);
# 		$("tdcp").appendChild(pobj);
# 	}
# 	addOptionTitle();
# }
# function GetProduct(bankid, boid) {
# 	var poid = boid.replace("cbs", "id");
# 	var url = '/action/simpleproduct.jspa';
# 	var params = 'bankid=' + bankid + "&poid=" + poid + "&wf=" + wf;
# 	var target = $(poid);
# 	var targetLength = $(boid.replace('cbs', 'id')).length;
# 	for ( var i = 1; i < targetLength; i++) {
# 		target.remove(1);
# 	}
# 	if (bankid > 0)
# 		new Ajax.Request(url, {
# 			method : 'post',
# 			parameters : params,
# 			onSuccess : getProductByBankID
# 		});
# }
# function getProductByBankID(request) {
# 	var action = request.responseJSON;
# 	var pobj = $(action.poid);
# 	for (j = 0; j < action.product.length; j++) {
# 		pobj.options[pobj.length] = new Option(action.product[j].productName,
# 				action.product[j].productID);
# 	}
# 	addOptionTitle();
# }
# function ChangeSelect4(location) {
# 	$('llresult').value = "";
# 	var objRateKind = $("ratekind");
# 	var objRateOpt = $("rateoption");
# 	switch (location) {
# 	case "0":
# 		objRateOpt.hide();
# 		objRateKind.length = 0;
# 		objRateKind.style.width = "75px";
# 		for (i = 0; i < RMBRate.length; i++) {
# 			if (RMBRate[i][1].substr(0, 2) == "02") {
# 				objRateKind.options[objRateKind.length] = new Option(
# 						RMBRate[i][0], RMBRate[i][1]);
# 			}
# 		}
# 		break;
# 	case "1":
# 		objRateOpt.hide();
# 		objRateKind.length = 0;
# 		objRateKind.style.width = "135px";
# 		for (i = 0; i < RMBRate.length; i++) {
# 			if (RMBRate[i][1].substr(0, 2) == "01") {
# 				objRateKind.options[objRateKind.length] = new Option(
# 						RMBRate[i][0], RMBRate[i][1]);
# 			}
# 		}
# 		break;
# 	case "2":
# 		objRateOpt.show();
# 		objRateKind.length = 0;
# 		objRateKind.style.width = "70px";
# 		for (i = 1; i < ForeignRate.length; i++) {
# 			objRateKind.options[objRateKind.length] = new Option(
# 					ForeignRate[i][0], i);
# 		}
# 		objRateOpt.length = 0;
# 		for (i = 1; i < ForeignRate[0].length - 1; i++) {
# 			objRateOpt.options[objRateOpt.length] = new Option(
# 					ForeignRate[0][i], i);
# 		}
# 		break;
# 	}
# 	ShowLLResult();
# }
# function ChangeSelect5(location) {
# 	$('llresult').value = "";
# 	var ratetype = $("ratetype");
# 	var type = ratetype.options[ratetype.selectedIndex].value;
# 	var objRateOpt = $("rateoption");
# 	if (location.substr(0, 4) == "0202" || location.substr(0, 4) == "0204") {
# 		objRateOpt.show();
# 		objRateOpt.length = 0;
# 		for (i = 0; i < RMBRateDQ.length; i++) {
# 			if (RMBRateDQ[i][0] == location) {
# 				objRateOpt.options[objRateOpt.length] = new Option(
# 						RMBRateDQ[i][1], RMBRateDQ[i][2]);
# 			}
# 		}
# 	} else {
# 		if (type == "2") {
# 			objRateOpt.show();
# 		} else {
# 			objRateOpt.hide();
# 		}
# 	}
# 	ShowLLResult();
# }
# function ShowLLResult() {
# 	var objRateKind = $("ratekind");
# 	var objresult = $("llresult");
# 	var objRatetype = $("ratetype");
# 	var rateoption = $("rateoption");
# 	var Kind = objRateKind.options[objRateKind.selectedIndex].value;
# 	var type = objRatetype.options[objRatetype.selectedIndex].value;
# 	switch (type) {
# 	case "0":
# 		if (Kind.length == 4 && Kind != "0204") {
# 			for (i = 0; i < RMBRate.length; i++) {
# 				if (RMBRate[i][1] == Kind) {
# 					objresult.value = RMBRate[i][2];
# 				}
# 			}
# 		} else {
# 			var OptDQ = rateoption.options[rateoption.selectedIndex].value;
# 			for (i = 0; i < RMBRateDQ.length; i++) {
# 				if (RMBRateDQ[i][2] == OptDQ) {
# 					objresult.value = RMBRateDQ[i][3];
# 				}
# 			}
# 		}
# 		break;
# 	case "1":
# 		for (i = 0; i < RMBRate.length; i++) {
# 			if (RMBRate[i][1] == Kind) {
# 				objresult.value = RMBRate[i][2];
# 			}
# 		}
# 		break;
# 	case "2":
# 		var Opt = rateoption.options[rateoption.selectedIndex].value;
# 		objresult.value = ForeignRate[Kind][Opt];
# 		break;
# 	}
# }
# function ShowHLResult() {
# 	var objHLType = $("exchangetype");
# 	var hltype = objHLType.options[objHLType.selectedIndex].value;
# 	var objresult = $("result");
# 	switch (hltype) {
# 	case "0":
# 		var objRMB = $("rmbchange");
# 		var rmbresult = objRMB.options[objRMB.selectedIndex].value;
# 		for (i = 0; i < RMB.length; i++) {
# 			if (RMB[i][1] == rmbresult) {
# 				objresult.value = RMB[i][2];
# 			}
# 		}
# 		break;
# 	case "1":
# 		var objForeign1 = $("foreignexchage1");
# 		var objForeign2 = $("foreignexchage2");
# 		var foreign1 = objForeign1.options[objForeign1.selectedIndex].value;
# 		var foreign2 = objForeign2.options[objForeign2.selectedIndex].value;
# 		objresult.value = ForeignEx[foreign1][foreign2];
# 		break;
# 	}
# }
# function ChangeSelect3(location) {
# 	$('result').value = '';
# 	var objRMB = $('rmbchange');
# 	var objForeign1 = $('foreignexchage1');
# 	var objForeign2 = $('foreignexchage2');
# 	switch (location) {
# 	case "0":
# 		$('result').style.width = "50px";
# 		objRMB.show();
# 		$('slash').hide();
# 		objRMB.length = 0;
# 		for (i = 0; i < RMB.length; i++) {
# 			objRMB.options[objRMB.length] = new Option(RMB[i][0] + "/人民币",
# 					RMB[i][1]);
# 		}
# 		break;
# 	case "1":
# 		$("ratetype").selectedIndex = 0;
# 		objRMB.hide();
# 		$('slash').show();
# 		objForeign1.length = 0;
# 		for (i = 1; i < ForeignEx[0].length - 1; i++) {
# 			objForeign1.options[objForeign1.length] = new Option(
# 					ForeignEx[0][i], i);
# 		}
# 		objForeign2.length = 0;
# 		for (i = 1; i < ForeignEx.length; i++) {
# 			objForeign2.options[objForeign2.length] = new Option(
# 					ForeignEx[i][0], i);
# 		}
# 		break;
# 	}
# 	ShowHLResult();
# }
# function changelen(value) {
# 	if (value == 11 || value == 12) {
# 		$("foreignexchage1").style.width = "70px";
# 		$('result').style.width = "45px";
# 	} else {
# 		$("foreignexchage1").style.width = "60px";
# 		$('result').style.width = "50px";
# 	}
# }
# function InitBankphone() {
# 	var objbp = $("telbank");
# 	objbp.length = 0;
# 	var j = 0;
# 	for (i = 0; i < bank.length; i++) {
# 		if (bank[i][2].length > 0) {
# 			if (j == 0)
# 				$("tel").value = bank[i][2];
# 			objbp.options[objbp.length] = new Option(bank[i][1], i);
# 			j++;
# 		}
# 	}
# }
# function ChangeSelect2(location) {
# 	$("tel").value = bank[location][2];
# }
# function fnOpen(strUrl) {
# 	window
# 			.open(
# 					strUrl,
# 					"",
# 					"width=595,height=345,status=yes,toolbar=no,menubar=no,location=no,scrollbars=auto,resizable=yes,top=190,left=250");
# }
# function mark(score, id, type) {
# 	var cp = new HttpCookie("cp_mark");
# 	if (cp.values.get(id) == "ok") {
# 		alert("您已经投过票了，谢谢您的参与！")
# 	} else {
# 		var cp = new HttpCookie("cp_mark");
# 		cp.values.set(id, "ok");
# 		cp.setExpires(365 * 24 * 60 * 60);
# 		cp.save();
# 		var url = '/action/grade.jspa';
# 		var params = "mark=" + score + "&oid=" + id + "&type=" + type;
# 		new Ajax.Request(url, {
# 			method : 'post',
# 			parameters : params,
# 			onSuccess : markresult
# 		});
# 	}
# }
# function markresult(request) {
# 	var res = request.responseJSON
# 	alert('感谢您的参与，该产品积分为' + res.result + "分");
# 	for ( var i = 0; i < frmscro.score.length; i++) {
# 		if (frmscro.score[i].checked) {
# 			frmscro.score[i].checked = false;
# 		}
# 	}
# }
# function isHasBankDetail(bankId) {
# 	for ( var i = 0; i < bank.length; i++) {
# 		if (bankId == bank[i][0]) {
# 			return true;
# 		}
# 	}
# 	return false;
# }
# function addOptionTitle() {
# 	var options = document.getElementsByTagName("option");
# 	for ( var i = 0; i < options.length; i++)
# 		options[i].title = options[i].innerHTML;
# }
# function dd(str, c) {
# 	return (str.replace(/([\u0391-\uffe5])/ig, '$1a').substring(0, c).replace(
# 			/([\u0391-\uffe5])a/ig, '$1'));
# }
# ///*功能： 得到两个日期相差的天数（每一个月按30天，一年360天计算）
# //入口参数：
# //			date1: 日期对象1
# //			date2: 日期对象2
# //			返回 date1 - date2相差的天数
# //*/
# //function getDiffDay(date1, date2) {
# //	var year = date1.getFullYear() - date2.getFullYear();
# //	var month = date1.getMonth() - date2.getMonth();
# //	var day = date1.getDate() - date2.getDate();
# //	return year * 12 * 30 + month * 30 + day;
# //}
# /*
# //字符串转换为日期
# //传入 yyyy-MM-dd
# //返回 Date 941644800000
# //*/
# //function Cal_strtodate(str) {
# //	var date = Date.parse(str);
# //	if (isNaN(date)) {
# //		date = Date.parse(str.replace(/-/g, "/"));
# //		if (isNaN(date)) {
# //			date = 0;
# //		}
# //	}
# //	return (date);
# //}