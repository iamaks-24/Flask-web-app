function deleteNote(noteId){
    fetch("/delete-note",{// sends post request to backebd(delete-note endpoint)
        method:"POST",
        body: JSON.stringify({noteId: noteId}),//returns as string
    }).then((res)=>{
        window.location.href="/";//once v get response from endpoint here it vl reload the window(refresh page)
    });
}