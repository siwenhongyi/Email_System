function addiclass()
{
    var filediv = $('.attfile');
    var n = filediv.length
    for(var i = 0;i<n;i++){
        var spanid = $(filediv[i]).attr('data-class');
        var name   = $(filediv[i]).attr('data-name');
        var suffix = suffixName(name).toLowerCase();
        console.log(suffix)
        if (suffix == '.jpg' || suffix == '.jpeg' || suffix == '.png' || suffix == '.bmp' || suffix == '.gif') { //图片格式
            res = 'appfile-image-o'
        } else if (suffix == '.doc' || suffix == '.docx') {//word格式
            res = 'appfile-word-o'
        } else if (suffix == '.xls' || suffix == '.xlsx') {//excel格式
            res = 'appfile-excel-o'
        } else if (suffix == '.ppt' || suffix == '.pptx') {//PPT格式
            res = 'appfile-ppt-o'
        }else if (suffix == '.pdf') {//PDF格式
            res = 'appfile-pdf-o'
        }else if (suffix == '.zip' || suffix == '.rar'|| suffix == '.7z') {//压缩格式
            res = 'appfile-com-o'
        }else if (suffix == '.wav' || suffix == '.mp3'|| suffix == '.aac'|| suffix == '.wma') {//声音格式
            res = 'appfile-audio-o'
        }else if (suffix == '.avi' || suffix == '.mp4'|| suffix == '.mov'|| suffix == '.mkv'||suffix == '.rm' || suffix == '.rmvb'|| suffix == '.mpg'|| suffix == '.mpeg') {//视频格式
            res = 'appfile-video-o'
        }else if (suffix == '.txt' ) {//文本格式
            res = 'appfile-text-o'
        }else {
            res = 'appfile-o'
        }
        $('#' + spanid).addClass(res);
    }
    return ;
}
function suffixName(file_name){
    var result = /\.[^\.]+/.exec(file_name);
    return result[0];
}