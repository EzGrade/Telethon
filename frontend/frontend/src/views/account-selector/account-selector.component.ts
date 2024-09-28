import {Component, OnInit} from '@angular/core';
import {NgForOf} from "@angular/common";
import {FormsModule} from "@angular/forms";

import {AccountsService, Account} from "../accounts.service";


@Component({
  selector: 'app-account-selector',
  standalone: true,
  imports: [
    NgForOf,
    FormsModule
  ],
  templateUrl: './account-selector.component.html',
  styleUrl: './account-selector.component.css'
})

export class AccountSelectorComponent implements OnInit {
  accounts: Account[] = [];

  constructor(private accountsService: AccountsService) {
  }

  ngOnInit() {
    this.accountsService.getAccounts().then(accounts => {
      this.accounts = accounts;
    }).catch(error => {
      return;
    });
  }

  selectAccount(account: Account) {
    this.accountsService.selectAccount(account);
  }
}
