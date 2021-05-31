function funciones_validarpassword(){
    if (document.getElementById('password').value == document.getElementById('confirmacion').value){
        console.log("contraseñas Iguales");

    }else{
        console.log("contraseñas Diferentes");
        VerificarContraseña();
        document.getElementById('password').value="";
        document.getElementById('confirmacion').value="";
        document.getElementById('password').focus();
    }
}