<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="CJDefault.aspx.cs" Inherits="ChallengeSimpleCalculator.CJDefault" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div style="font-family: Arial, Helvetica, sans-serif">
    
    &nbsp;<asp:Label ID="Title" runat="server" Font-Bold="True" Font-Names="Arial" Font-Size="XX-Large" Text="Simple Calculator"></asp:Label>
        <br />
        <br />
&nbsp;First Value:&nbsp;
        <asp:TextBox ID="SvalueTextBox" runat="server"></asp:TextBox>
        <br />
        <br />
        Second Value:&nbsp;
        <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
        <br />
        <br />
        <br />
        <asp:Button ID="AddButton" runat="server" Font-Bold="True" Text="+" Width="33px" />
&nbsp;&nbsp;&nbsp;&nbsp;
        <asp:Button ID="Button1" runat="server" Font-Bold="True" Text="-" Width="33px" />
&nbsp;&nbsp;&nbsp;&nbsp;
        <asp:Button ID="Button2" runat="server" Font-Bold="True" Text="*" Width="31px" />
&nbsp;&nbsp;&nbsp;&nbsp;
        <asp:Button ID="Button3" runat="server" Font-Bold="True" Text="/" Width="32px" />
        <br />
        <br />
        <br />
        <asp:Label ID="resultLabel" runat="server" BackColor="#6699FF" Font-Bold="True" Font-Size="Larger"></asp:Label>
    
    </div>
    </form>
</body>
</html>
