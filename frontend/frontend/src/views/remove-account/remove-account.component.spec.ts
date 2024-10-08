import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RemoveAccountComponent } from './remove-account.component';

describe('RemoveAccountComponent', () => {
  let component: RemoveAccountComponent;
  let fixture: ComponentFixture<RemoveAccountComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RemoveAccountComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(RemoveAccountComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
