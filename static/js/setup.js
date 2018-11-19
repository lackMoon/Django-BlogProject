function upload_image_layer() {
            layer.open({
                title:"上传头像",
                area:['650px','600px'],
                type:2,
                content:'/account/user-image/',
            });
}

function add_column() {
    var index = layer.open({
        type: 1,
        skin: "layui-layer-rim",
        area: ["400px", "200px"],
        title: "新增栏目",
        content: "<div class='text-center' style='margin-top:20px'>" + "<p>请输入新的栏目名称</p>" + "<p><input type='text' id='id_column' /></p>" + "</div>",
        btn: ['确定', '取消'],
        yes: function (index, layero) {
            column_name = $('#id_column').val();
            $.ajax({
                url:"/article/article-column/",
                type:"POST",
                data:{"column":column_name},
                success:function (e) {
                    if(e=="1"){
                        parent.location.reload();
                        layer.msg("增加栏目成功");
                    }else {
                        layer.msg("此栏目已有，请更换名称");
                    }
                },
            });
        },
        btn2: function (index, layero) {
            layer.close(index);
        },
    });
}

function edit_column(the,column_id) {
    var name=$(the).parents("tr").children("td").eq(1).text();
    var index=layer.open({
        type:1,
        skin:"layui-layer-rim",
        area:["400px","200px"],
        title:"编辑栏目",
        content:"<div class='text-center' style='margin-top:20px'>" + "<p>请输入新的栏目名称</p>" + "<p><input type='text' id='new_name' value='"+name+"' /></p>" + "</div>",
        btn: ['确定', '取消'],
        yes: function (index, layero) {
            new_name = $('#new_name').val();
            $.ajax({
                url:"/article/rename-column/",
                type:"POST",
                data:{"column_id":column_id,"column_name":new_name},
                success:function (e) {
                    if(e=="1"){
                        parent.location.reload();
                        layer.msg("编辑名称成功");
                    }else {
                        layer.msg("新名称未保存，编辑失败");
                    }
                },
            })
        },
        btn2: function (index, layero) {
            layer.close(index);
        },
    });
}

function del_column(the,column_id) {
    var name=$(the).parents("tr").children("td").eq(1).text();
    layer.open({
        type:1,
        skin:"layui-layer-rim",
        area:["400px","200px"],
        title:"删除栏目",
        content: "<div class='text-center' style='margin-top:20px'>" + "<p>是否删除["+name+"]栏目</p>" + "</div>",
         btn: ['确定', '取消'],
        yes: function () {
            $.ajax({
                url:"/article/del-column/",
                type:"POST",
                data:{"column_id":column_id},
                success:function (e) {
                    if(e=="1"){
                        parent.location.reload();
                        layer.msg("栏目成功删除");
                    }else {
                        layer.msg("删除失败");
                    }
                },
            })
        },
    btn2: function (index, layero) {
            layer.close(index);
        },
    });
}

function publish_article() {
    var title=$("#id_title").val();
    var column_id=$("#which_column").val();
    var body=$("#id_body").val();
    $.ajax({
        url:"/article/article-post/",
        type:"POST",
        data:{"title":title,"column_id":column_id,"body":body},
        success:function (e) {
            if(e=="1"){
                layer.msg("发布成功");
            }else if(e=="0"){
                layer.msg("发布失败");
            }else{
                layer.msg("填写字段不能为空");
            }
        },
    });
}
