function upFile(a) {
    var flag = $(a);
    if (!flag[0].files || !flag[0].files[0]) {
        return;
    }
    var name = flag[0].files[0].name;
    if($('#theme').attr('value').length == 0){
        $('#theme').attr('value',name);
    }
    var suffix =suffixName(name)[0].toLowerCase(); //后缀名
    var size = flag[0].files[0].size;  //文件大小
    var fr = new FileReader(); // 这个FileReader应该对应于每一个读取的文件都需要重新new一个
    var files = flag[0].files[0]; // files可以获取当前文件输入框中选择的所有文件，返回列表
    fr.readAsDataURL(files); // 读取的内容是加密以后的本地文件路径
    fr.onload = function (e) { // 数据读取完成时触发onload对应的响应函数
        var timeStamp = Math.floor(Math.random() * 10000); //自定义一个随机数
        $(flag).parent().addClass('li' + timeStamp).hide(); //每次隐藏之前添加一个Class
        var cou = $('.subfilesul li').length * 1
        var html = '<a href="javascript:void(0)" class="file" >上传附件\n' +
                   '    <input class="appfile" type="file" onchange="upFile(this)" name="' + (cou + 1) + '"/>\n' +
                   '</a>';
        $('.no_file').before(html);//每次生成一个input file  插入到节点

        var li;
        if (suffix == '.jpg' || suffix == '.jpeg' || suffix == '.png' || suffix == '.bmp' || suffix == '.gif') { //图片格式
            li = '<li><span><i class="fa appfile-image-o">&nbsp;</i>&nbsp;&nbsp;&nbsp;' + name + '</span> <span class="size">&nbsp;&nbsp;&nbsp;' + parseInt(files.size / 1000) + 'kb&nbsp;&nbsp;&nbsp;</span> <span class="remove" data-class="li' + timeStamp + '" onclick="deleteLi(this)">删除</span> </li>';
        } else if (suffix == '.doc' || suffix == '.docx') {//word格式
            li = '<li><span><i class="fa appfile-word-o">&nbsp;</i>&nbsp;&nbsp;&nbsp;' + name + '</span> <span class="size">&nbsp;&nbsp;&nbsp;' + parseInt(files.size / 1000) + 'kb&nbsp;&nbsp;&nbsp;</span> <span class="remove" data-class="li' + timeStamp + '" onclick="deleteLi(this)">删除</span> </li>';
        } else if (suffix == '.xls' || suffix == '.xlsx') {//excel格式
            li = '<li><span><i class="fa appfile-excel-o">&nbsp;</i>&nbsp;&nbsp;&nbsp;' + name + '</span> <span class="size">&nbsp;&nbsp;&nbsp;' + parseInt(files.size / 1000) + 'kb&nbsp;&nbsp;&nbsp;</span> <span class="remove" data-class="li' + timeStamp + '" onclick="deleteLi(this)">删除</span> </li>';
        } else if (suffix == '.ppt' || suffix == '.pptx') {//PPT格式
            li = '<li><span><i class="fa appfile-ppt-o">&nbsp;</i>&nbsp;&nbsp;&nbsp;' + name + '</span> <span class="size">&nbsp;&nbsp;&nbsp;' + parseInt(files.size / 1000) + 'kb&nbsp;&nbsp;&nbsp;</span> <span class="remove" data-class="li' + timeStamp + '" onclick="deleteLi(this)">删除</span> </li>';
        }else if (suffix == '.ppt' || suffix == '.pdf') {//PDF格式
            li = '<li><span><i class="fa appfile-pdf-o">&nbsp;</i>&nbsp;&nbsp;&nbsp;' + name + '</span> <span class="size">&nbsp;&nbsp;&nbsp;' + parseInt(files.size / 1000) + 'kb&nbsp;&nbsp;&nbsp;</span> <span class="remove" data-class="li' + timeStamp + '" onclick="deleteLi(this)">删除</span> </li>';
        }else if (suffix == '.zip' || suffix == '.rar'|| suffix == '.7z') {//压缩格式
            li = '<li><span><i class="fa appfile-com-o">&nbsp;</i>&nbsp;&nbsp;&nbsp;' + name + '</span> <span class="size">&nbsp;&nbsp;&nbsp;' + parseInt(files.size / 1000) + 'kb&nbsp;&nbsp;&nbsp;</span> <span class="remove" data-class="li' + timeStamp + '" onclick="deleteLi(this)">删除</span> </li>';
        }else if (suffix == '.wav' || suffix == '.mp3'|| suffix == '.aac'|| suffix == '.wma') {//声音格式
            li = '<li><span><i class="fa appfile-audio-o">&nbsp;</i>&nbsp;&nbsp;&nbsp;' + name + '</span> <span class="size">&nbsp;&nbsp;&nbsp;' + parseInt(files.size / 1000) + 'kb&nbsp;&nbsp;&nbsp;</span> <span class="remove" data-class="li' + timeStamp + '" onclick="deleteLi(this)">删除</span> </li>';
        }else if (suffix == '.avi' || suffix == '.mp4'|| suffix == '.mov'|| suffix == '.mkv'||suffix == '.rm' || suffix == '.rmvb'|| suffix == '.mpg'|| suffix == '.mpeg') {//视频格式
            li = '<li><span><i class="fa appfile-video-o">&nbsp;</i>&nbsp;&nbsp;&nbsp;' + name + '</span> <span class="size">&nbsp;&nbsp;&nbsp;' + parseInt(files.size / 1000) + 'kb&nbsp;&nbsp;&nbsp;</span> <span class="remove" data-class="li' + timeStamp + '" onclick="deleteLi(this)">删除</span> </li>';
        }else if (suffix == '.txt' ) {//文本格式
            li = '<li><span><i class="fa appfile-text-o">&nbsp;</i>&nbsp;&nbsp;&nbsp;' + name + '</span> <span class="size">&nbsp;&nbsp;&nbsp;' + parseInt(files.size / 1000) + 'kb&nbsp;&nbsp;&nbsp;</span> <span class="remove" data-class="li' + timeStamp + '" onclick="deleteLi(this)">删除</span> </li>';
        }else {
            li = '<li><span><i class="fa appfile-o">&nbsp;</i>&nbsp;&nbsp;&nbsp;' + name + '</span> <span class="size">&nbsp;&nbsp;&nbsp;' + parseInt(files.size / 1000) + 'kb&nbsp;&nbsp;&nbsp;</span> <span class="remove" data-class="li' + timeStamp + '" onclick="deleteLi(this)">删除</span> </li>';
        }
        if ($('.subfilesul li').length < 10) {  //判断不能超过10个  可自行写入多少
            $('.subfilesul').append(li);
            $('#count').attr('value',$('.subfilesul li').length);
        } else {
            pageCommon.layerMsg("最多能选择10个附件", 2, true)
        }

        if ($('.subfilesul li').length != 0) {  // 显示隐藏 未选择文件字眼
            $('.no_file').hide();
        } else {
            $('.no_file').show();
        }
    };
}

function deleteLi(a) {
    $(a).parent().remove();
    var attr = $(a).attr('data-class');
    var newAttr = '.' + attr;
    $('.files ' + newAttr).remove(); //删除对应 input file
    $('#count').attr('value',$('.subfilesul li').length);
    if ($('.subfilesul li').length != 0) { // 显示隐藏 未选择文件字眼
        $('.no_file').hide();
    } else {
        $('.no_file').show();
    }  
}

function suffixName(file_name){
    var result = /\.[^\.]+/.exec(file_name);
    return result;
}
function checkmail() {
    var re = document.getElementsByName('first')[0].value
    if(re.length == 0){
        alert('收件人不能为空')
        return false;
    }
    var theme = document.getElementsByName('second')[0].value;
    var con = document.getElementsByName('last')[0].value
    if (theme.length + con.length == 0){
        alert('主题内容不能全为空')
        return false;
    }
    $('#sendbtn').attr('disabled',true);
    return true;
}