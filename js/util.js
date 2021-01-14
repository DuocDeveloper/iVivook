function validaLogin(){
    var nombreUsuario = document.getElementById('txtNombreUsuario');
    var contraseña = document.getElementById('txtContraseña');

    if(nombreUsuario.value == ""){
        alert("Ingrese su nombre de usuario");
        nombreUsuario.focus();
        return false;
    }

    if(contraseña.value == ""){
        alert("Ingrese su contraseña");
        contraseña.focus();
        return false;
    }
}