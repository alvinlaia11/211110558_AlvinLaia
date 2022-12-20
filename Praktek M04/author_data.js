class AuthorData {
    constructor() {
        this.getDataList();
        this.leftright();
    }
    pageNumber = 1;
    getDataList(){
        var sbutton = document.getElementById('sbutton');
        var lbutton = document.getElementById('lbutton');
        sbutton.addEventListener('click', () => {
            this.pageNumber--;
            console.log("Arah ke Kiri <<")
            this.getProfile().then(data => {
                this.showProfile(data);
                this.leftright(data);
            }).catch(e => console.log(e));
        });
        lbutton.addEventListener('click', () => {
            this.pageNumber++;
            console.log("Arah ke Kanan >>")
            this.getProfile().then(data => {
                this.showProfile(data);
                this.leftright(data);
            }).catch(e => console.log(e));
        });
    }
    async getProfile(){
        let pageNumber = this.pageNumber;
        let url = `https://picsum.photos/v2/list?page=${pageNumber}&limit=1`;
        console.log(url)
        let response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return await response.json();
    }
    showProfile(obj){
        let data_div = document.getElementById("image");
        let data_string = document.getElementById("authorfix");
        obj.forEach((result) => {
            data_string.innerHTML = `${result.author}`;
            data_div.innerHTML = `<img src="${result.download_url}" class="mt-2" width="300" height="200">`;
        });
    }
    leftright(){
        var kbutton = document.getElementById("sbutton");
        var knbutton = document.getElementById("lbutton");

        if(this.pageNumber <= 1 ){
            kbutton.disabled = true;
        }else if(this.pageNumber == 2){
            kbutton.disabled = false;
        }

        if (this.pageNumber >= 993) {
            knbutton.disabled = true;
        }else if(this.pageNumber == 992)    {
            knbutton.disabled = false;
        }
    }
}
export default AuthorData;
