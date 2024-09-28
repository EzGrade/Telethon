import {Injectable} from '@angular/core';
import {BACKEND_IP} from "../globals";
import {HttpClient} from "@angular/common/http";

export interface Account {
  id: number;
  telegram_id: string;
  username: string;
  channels: string[];
  selected: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class AccountsService {
  accounts: Account[] = [];

  constructor(private http: HttpClient) {
  }

  getAccounts(): Promise<Account[]> {
    return new Promise((resolve, reject) => {
      this.http.get<Account[]>(BACKEND_IP + '/api/telegram-accounts/').subscribe(
        accounts => {
          this.accounts = accounts;
          resolve(this.accounts);
        },
        error => {
          reject(error);
        }
      );
    });
  }

  selectAccount(account: Account) {
    account.selected = !account.selected;
  }
}
