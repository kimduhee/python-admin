const getAjaxData = (ajaxUrl, ajaxData, callback) => {
    $.ajax({
        url: ajaxUrl,
        method: 'post',
        data : JSON.stringify(ajaxData),
        contentType : "application/json",
        //dataType : 'json',
        success: (data, status, xhr) => {
            callback(data);
        },
        error: (data, status, err) => {
            console.log(err);
        },
        complete: () => {
        }
    });
}

const pagingCreate = (pageNo, totalPageNo) => {

      let startPage = (parseInt(pageNo/10)*10) + 1;
      let endPage = (startPage + 9) > totalPageNo?totalPageNo:startPage + 9;

      console.log("startPage:" + startPage);
      console.log("endPage:" + endPage);

      let pagehtml = "";
      pagehtml += '<div class="col-sm-12 col-md-7">';
      pagehtml += ' <div class="dataTables_paginate paging_simple_numbers">';
      pagehtml += '   <ul class="pagination">';

      //첫 페이지
      pagehtml += '     <li class="paginate_button page-item previous"><a href="#" class="page-link"><<</a></li>';
      
      //이전 페이지
      if(pageNo == 1 || totalPageNo == 1) {
        pagehtml += '     <li class="paginate_button page-item previous disabled"><a href="#" class="page-link"><</a></li>';
      } else {
        pagehtml += '     <li class="paginate_button page-item previous"><a href="#" class="page-link"><</a></li>';
      }

      //페이지 처리
      for(var i=startPage;i<endPage+1; i++) {
        if(i==pageNo) {
          pagehtml += '     <li class="paginate_button page-item active"><a href="javascript:void(0);" class="page-link">'+i+'</a></li>';
        } else {
          pagehtml += '     <li class="paginate_button page-item"><a href="#" class="page-link">'+i+'</a></li>';
        }
      }

      //다음 페이지
      if(totalPageNo > pageNo) {
        pagehtml += '     <li class="paginate_button page-item next"><a href="#" class="page-link">></a></li>';
      } else {
        pagehtml += '     <li class="paginate_button page-item next disabled"><a href="#" class="page-link">></a></li>';
      }

      //마지막 페이지
      pagehtml += '     <li class="paginate_button page-item next"><a href="#" class="page-link">>></a></li>';

      pagehtml += '   </ul>';
      pagehtml += ' </div>';
      pagehtml += '</div>';

      return pagehtml;
    }