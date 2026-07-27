import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

// `providedIn: 'root'` registers this as a singleton service in Angular's
// root injector, so any component can inject it via the constructor
// without needing to list it in a module's providers array.
@Injectable({
  providedIn: 'root',
})
export class Course {
  // Angular's DI (dependency injection) hands us a shared HttpClient instance here.
  constructor(private http: HttpClient) { }

  getCourses() {
    // Returns an Observable — callers must .subscribe() to actually trigger the request.
    return this.http.get<any[]>('https://jsonplaceholder.typicode.com/posts?_limit=5');
  }
}
