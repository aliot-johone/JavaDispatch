
function radioBind(formId){
	var radioName =[];
	$('#'+formId).find('input[type="radio"]').each(function(){
		radioName[$(this).prop('name')]=1;
	});
	for(name in radioName){
		var hid = getRadioHidden(name);
		var val = hid.val()
		console.log(name)
		console.log('hid val='+val)
		$('input[name="'+name+'"]').each(function(){
			var checked = (val==$(this).val());
			if(checked){
				$(this).prop("checked",'checked'); 
			}else{
				$(this).removeAttr("checked");
			}
			
		});
	}
}

function getRadioHidden(radioName){
	return $('#'+radioName+'Hidden');
}
