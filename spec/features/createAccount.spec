###########################
#
# If this website did not have a captcha verification the submission form
# wouldve been designed and developed like this
#
###########################
feature "User Sign up" do
  before(:each) do
    visit_home_pg
    visit_signIn_signUp_pg
    expect(page).to have_content("Login")
  end

  describe "fill outs user sign up form" do
    xit "creates a new user w/o sign up newsletter" do
      new_signup_form = ::CreateAccount::AccountForm.new
      new_signup_form.create_new_account.fill_in_with(
        FirstName: Faker::Name.unique.first_name,
        LastName: Faker::Name.unique.last_name,
        Email: Faker::Internet.email,
        CreatePassword: "p@ssword",
      ).submit

      
    end

    xit "creates a new user w/ sign up newsletter" do
      new_signup_form = ::CreateAccount::AccountForm.new
      new_signup_form.create_new_account.fill_in_with(

        FirstName: Faker::Name.unique.first_name,
        LastName: Faker::Name.unique.first_name,
        Email: Faker::Internet.email,
        CreatePassword: "p@ssword",
      ).check_news_letter.submit
    end
  end
end
