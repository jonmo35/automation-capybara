feature "Login Logout" do
  before(:each) do
    visit_home_pg
    visit_signIn_signUp_pg
    expect(page).to have_content("Login")
  end

  describe "qa user account" do
    it "logins qa user account" do
      login = ::LoginHelper::LoginUser.new
      login.login_form(
        CustomerEmail: "rtassessment@gmail.com",
        CustomerPassword: "!f33db@ck!",
      ).login_button

      expect(find(class: "page-title")).to have_text("My Account")
      expect(current_url).to eq "https://www.gouletpens.com/account"
    end

    it "log outs qa user account" do
      login = ::LoginHelper::LoginUser.new
      login.login_form(
        CustomerEmail: "rtassessment@gmail.com",
        CustomerPassword: "!f33db@ck!",
      ).login_button

      click_link("Sign Out", :href => "/account/logout")
      expect(current_url).to eq "https://www.gouletpens.com/"
      within("#header__account-nav-link--account") do
        expect(find("span")).to have_text("Sign In / Sign Up")
      end
    end
  end
end
