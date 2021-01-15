function validaLogin(){
    var nombreUsuario = document.getElementById('txtRut');
    var contraseña = document.getElementById('txtContraseña');

    if(nombreUsuario.value == ""){
        alert("Ingrese su rut");
        nombreUsuario.focus();
        return false;
    }

    if(contraseña.value == ""){
        alert("Ingrese su contraseña");
        contraseña.focus();
        return false;
    }
}

$(function(){
    $("#btnLimpiar").click(function(){
        $('input').val('');
    });
})

