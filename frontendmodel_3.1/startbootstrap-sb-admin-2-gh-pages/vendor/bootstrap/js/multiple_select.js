// 判断是否选中 
function anyChecked(){
                    
    var elements=document.form1.elements; // form1为表单name的值
    var counter=elements.length;
    for(var i=0;i<counter;i++){
        var element=elements[i];
        alert();
        if(element.checked == true){
                alert(element.value);
         return true;
        }
    }
    return false;
} 

//多选 
 
var checklist = document.getElementsByName ("controlAll");
    for(var i=0;i<checklist.length;i++){
            if(checklist[i].checked == true && i == checklist.length-1){
            id = id + checklist[i].value;
                }else if(checklist[i].checked == true){
            id = id + checklist[i].value + ',';
                }   
    }         

 //全选
 function ckAll(){
    var flag=document.getElementById("allChecks").checked;
    var cks=document.getElementsByName("check");
    for(var i=0;i<cks.length;i++){
        cks[i].checked=flag;
    }
}