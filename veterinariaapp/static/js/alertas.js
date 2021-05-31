function VerificarContraseña(){
	 $.alert({
			 closeIcon: true,
			 type: 'blue',
			 icon: 'glyphicon glyphicon-warning-sign',
			 title: 'Confirmación',
			 content: 'Confirmación de Contraseña Incorrecta',
			 buttons: {
			 OK: function () {
                btnClass: 'btn-blue',
               document.location.href = '#';
            },
        }
    });
}
function confirmaEliminar(purl){
    console.log(purl);
    $.confirm({
        title: 'Confirmación',
        content: '¿Desea eliminar el registro?',
        type: 'orange',
        icon: 'glyphicon glyphicon-warning-sign',
        buttons: {
            Eliminar: function () {
                console.log(purl);
                document.location.href = purl;
            },
            Cancelar: function () {
                document.location.href = '#';
            }
        }
    });
}