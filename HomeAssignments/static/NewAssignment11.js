function getUser(){
    var id_input = document.getElementById('id_num').value;
    console.log(id_input);
    fetch(`https://reqres.in/api/users/${id_input}`).then(
        response => response.json()
    ).then(
        response_obj => put_user_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_user_inside_html(response_obj_data){
    console.log(response_obj_data)
    const curr_main = document.querySelector("main");
    while (curr_main.firstChild) {
        curr_main.removeChild(curr_main.lastChild);
    }
    // for (let user of response_obj_data) {
    const section = document.createElement('section');
    // the sign ` is to use $
    section.innerHTML = `        
    <img src="${response_obj_data.avatar}" alt="Profile picture"/>
    <div>
       <span> ${response_obj_data.first_name} ${response_obj_data.last_name} </span>
       <br>
       <a href="mailto:${response_obj_data.email}"> send email </a>
    </div> `;
    curr_main.appendChild(section);
}