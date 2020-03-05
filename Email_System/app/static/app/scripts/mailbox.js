function mail_open(a)
{
    var opentype = $(a).attr('class');
    u = 'http://' + window.location.host + '/mail?mid=' + $(a).attr('data-class');
    if(opentype=="mailtb")
        window.location.href = u;
    else{
        event.stopPropagation();
        window.open(url = u);
    }
}