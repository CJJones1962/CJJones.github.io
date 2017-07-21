using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace MyFirstChallenge
{
    public partial class MyFirstChallenge : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void okButton_Click(object sender, EventArgs e)
        {
            string firstName = firstNameTextBox.Text;
            string lastName = lastNameTextBox.Text;

            string age = ageBox.Text;
            string money = moneyBox.Text;

            string result = "Wow! " + firstName + " At " + age + " years old, I would have expected you to have more than " + money + " in your pocket. ";

            resultLabel.Text = result;
        }
    }
}