$(document).ready(function(){

	$("#signup").click(function(){
        var name = $("#name").val();
        var email = $("#email").val();
        var phone = $("#number").val();
        var age = $("#age").val();
        var password = $("#pass").val();
        var gender = $("input[name='gender']:checked").val();
        
		$.ajax({
			url: '/save/',
			method: 'POST',
			data: {
                    'name': name,
                    'age' : age,
                    'gender' : gender,
                    'phone' : phone,
                    'email' : email,
                    'password' : password
				  },
			dataType:'json',
			success: function () {
					alert("Registered successfully!");
					}
		});
    });

});