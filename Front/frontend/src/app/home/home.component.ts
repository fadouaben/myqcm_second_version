import { Component,OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit{

  constructor(private http:HttpClient){}

  obj:any;

  ngOnInit(): void {
      this.obj = this.http.get('http://127.0.0.1:8000/user/').subscribe(
        data => this.obj = data
      );
  }

}
