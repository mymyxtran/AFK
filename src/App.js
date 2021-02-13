import logo from './logo.svg';
import './App.css';
import React from 'react';
import { Button } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import Box from '@material-ui/core/Box';
import { createMuiTheme, ThemeProvider, withStyles } from '@material-ui/core/styles';
import background from "./blue-css.jpg";

const theme = createMuiTheme({
  palette: {
    primary: {
      main: '#2574B6',
    },
    secondary: {
      main: '#82b1ff',
    },
  },
});

const defaultProps = {
  bgcolor: 'background.paper',
  m: 1,
  border: 1,
  style: { width: '5rem', height: '5rem' },
};

const useStyles = makeStyles((theme) => ({
  root: {
    '& > *': {
      margin: theme.spacing(1),
      width: '25ch',
    },
  },
  backgroundStyle: {
    backgroundImage: `url(${background})`,
  },
}));

function App() {
  const classes = useStyles();
  const [typeClothing, setTypeClothing] = React.useState('');

  return (
    <div className="App">
       <ThemeProvider theme={theme}>
      <AppBar position="sticky" style = { {backgroundColor: "#2574B6"} }>
        <Toolbar>
          <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" className={classes.title}>
            a fashion knomad
          </Typography>
          {/* <Button color="inherit">Login</Button> */}
        </Toolbar>
      </AppBar>
      <Box p={40} bgcolor="background.paper" className={classes.backgroundStyle}>
        <Button color = "primary" > Sustainable alternatives exist. We can find it for you. </Button>
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />    
          <ClothingTypeInputForm />
            {/* <form className={classes.root} noValidate autoComplete="off">
                <TextField  required id="standard-required" label="Input the clothing article's url" />
            </form>    */}
      </Box> 
      </ThemeProvider>
    </div>
  );
}

class ClothingTypeInputForm extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    // const { classes } = this.props;
    return (
      <form onSubmit={this.handleSubmit} Validate autoComplete="off">
        {/* className={classes.root} */}
          <TextField  value={this.state.value} onChange={this.handleChange} required id="standard-required" label="Clothing Type" />
      </form>
    );
  }
}

export default App;

