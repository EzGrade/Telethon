import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BACKEND_IP } from '../../globals';
import { AccountsService } from '../accounts.service';
import { forkJoin } from 'rxjs';

@Component({
  selector: 'app-remove-account',
  standalone: true,
  imports: [],
  templateUrl: './remove-account.component.html',
  styleUrl: './remove-account.component.css'
})
export class RemoveAccountComponent {
  constructor(private http: HttpClient, private accountsService: AccountsService) {}

  removeAccount() {
    const selectedAccounts = this.accountsService.accounts.filter(account => account.selected);
    const deleteRequests = selectedAccounts.map(account =>
      this.http.delete(BACKEND_IP + '/api/telegram-accounts/' + account.id + '/')
    );

    forkJoin(deleteRequests).subscribe(() => {
      this.accountsService.getAccounts();
      window.location.reload();
    });
  }
}
