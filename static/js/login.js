$(function(){
	$('#username').focus().blur(checkName);
	$('#password').blur(checkPassword);
});

function checkName(){
	var name = $('#username').val();
	if(name == null || name == ""){
		//提示错误
		$('#count-msg').html("姓名不能为空");
		return false;
	}
	$('#count-msg').empty();
	return true;
}

function checkPassword(){
	var password = $('#password').val();
	if(password == null || password == ""){
		//提示错误
		$('#password-msg').html("身份证号不能为空");
		return false;
	}
	$('#password-msg').empty();
	return true;
}

$("#login").submit(function(e){
	e.preventDefault(event);
	var name = $('#username').val();
	var password = $('#password').val();
	fetch('/search', {
		method: 'post',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			name,
			password
		})
	})
	.then(response => response.json())
  .then(data => {

  		if(data.code == 200) {
  			$("#logo").text("考生信息");
			$("#login-form").empty();
			$("#login-form").html(
			`<ul>
				<li><span>姓名:<span><span>${data.data.username}<span></li>
				<li><span>身份证号:<span><span>${data.data.userid}<span></li>
				<li><span>准考证号:<span><span>${data.data.examinee_number}<span></li>
				<li><span>岗位名称:<span><span>${data.data.title_name}<span></li>
				<a href="/download/${data.data.userid}" target="_blank"><li><span>查看准考证<span></li></a>
			</ul>`
		);}
  		else {
  			$('#check-msg').html(data.msg);
			return false;
		}
  });
});