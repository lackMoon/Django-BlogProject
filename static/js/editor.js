$(function () {
    var editor=editormd("editormd",{
        width:750,
        height:750,
        syncScrolling:"single",
        path:"{% static 'editor/lib/' %}"
    });
});