import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import {AccountSelectorComponent} from "../views/account-selector/account-selector.component";
import {ActionSelectorComponent} from "../views/action-selector/action-selector.component";

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, AccountSelectorComponent, ActionSelectorComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';
}
