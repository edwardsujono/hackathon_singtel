$(function(){
    $("#submit_button").click(
        function(event){
            event.preventDefault();
            console.log("click the submit button");
            window.location.href = '/collect_or_deposit';
        }
    );
});