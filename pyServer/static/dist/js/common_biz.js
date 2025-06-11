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