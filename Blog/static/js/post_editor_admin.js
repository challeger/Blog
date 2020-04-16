(function ($) {
    const $content_md = $("#id_content_md");
    const $content_ck = $("#id_content_ck");
    const $is_md = $('input[name=is_md]');
    const switch_editor = function (is_md) {
        if (is_md){
            $content_md.show();
            $content_ck.hide();
        } else{
            $content_md.hide();
            $content_ck.show();
        }
    };
    $is_md.on('click', function () {
        switch_editor($(this).is(':checked'));
    });
    switch_editor($is_md.is(':checked'));
})(jQuery);