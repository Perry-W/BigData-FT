//Check all method1
function All(e, itemName)
{
    var aa = document.getElementsByName(itemName);
    for (var i=0; i < aa.length; i++)

        aa[i].checked = e.checked; //得到那个总控的复选框的选中状态  
}
  
//Single select
function Item(e, allName)
{
    var all = document.getElementsByName(allName)[0];
    if(!e.checked) all.checked = false;
    else
    {
        var aa =document.getElementsByName(e.name);
        for (var i=0; i<aa.length; i++)
            if(!aa[i].checked) return;
        all.checked= true;
    }
}


// 判断是否选中 method2
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
function checkChange(element){ 
var checklist = document.getElementsByName ("controlAll");
    for(var i=0;i<checklist.length;i++){
            if(checklist[i].checked == true && i == checklist.length-1){
            id = id + checklist[i].value;
                }else if(checklist[i].checked == true){
            id = id + checklist[i].value + ',';
                }   
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

//全选 method3
 
function selectAll(){
 
                   
    var checklist = document.getElementsByName ("controlAll");
      if(document.getElementById("selectAll").checked)
      {
              for(var i=0;i<checklist.length;i++)
              {
                 checklist[i].checked = 1;
                 if(i == checklist.length-1){
                         id = id + checklist[i].value;
                      }else{
                                 id = id + checklist[i].value + ',';
                      }
                 
              } 
             
     }else{
             for(var j=0;j<checklist.length;j++)
             {
                checklist[j].checked = 0;
             }
             id = "";
     }
   }