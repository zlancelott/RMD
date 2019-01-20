function toggleBtn(botao){
	var elemento;
	switch(botao){
		case 1: elemento = $(".btnPesquisarInput input"); break;
		case 2: elemento = $(".btnMaisBotoesGrupo"); break;
		//case 3: Clique aqui para saber mais sobre o diálogo!
		}

	if(elemento.is(":visible")){
		elemento.hide(300);
	}else{
		elemento.show(300);
		// elemento.focus(); -- Focar o campo caso seja texto
	}

	// Se quiser que o botão pesquisa feche ao desfocar o input
	// $(".btnPesquisarInput input").blur(function(){ toggleBtn(1); });
}

$(".btnPesquisarBtn button, .btnMaisBotoesBtn button, .btnSupEsquerdo button").click(function(){
	var botao = $(this).attr("name");
	botao = parseInt(botao);
	toggleBtn(botao);
});
