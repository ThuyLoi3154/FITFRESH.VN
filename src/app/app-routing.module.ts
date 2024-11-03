import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  // các route khác
  { path: '', redirectTo: '/login', pathMatch: 'full' } // hoặc đường dẫn chính xác bạn muốn hiển thị đầu tiên
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
