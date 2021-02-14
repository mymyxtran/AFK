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
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import MenuIcon from '@material-ui/icons/Menu';
import Box from '@material-ui/core/Box';
import { createMuiTheme, ThemeProvider, withStyles } from '@material-ui/core/styles';
import background from "./bg.jpg";
import Chart from './Components/charts';
import Table from "./Components/table"
import thelowerbackground from "./bg-question.png"

const imagesPath = {
  minus: "bg.jpg",
  plus: "bg-beige.png"
}

const theme = createMuiTheme({
  palette: {
    primary: {
      main: '#fffff',
    },
    secondary: {
      main: '#82b1ff',
    },
    typography: {
      allVariants: {
        color: "#000000",
      },
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
  backgroundStyle2: {
    backgroundImage: `url(${thelowerbackground})`,
  },
  root: {
    flexGrow: 1
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: "center",
    color: theme.palette.text.secondary
  },
}));

function App() {
  const classes = useStyles();
  const [typeClothing, setTypeClothing] = React.useState('');

  return (
    <div className="App">
       <ThemeProvider theme={theme}>
      <AppBar position="sticky" style = { {backgroundColor: "#FFFFFF"} }>
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
      <Box p={33} bgcolor="background.paper" className={classes.backgroundStyle}>
        <Button color = "primary" > Sustainable alternatives exist. We can find it for you. </Button>
          <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />    
          <ClothingTypeInputForm />
            {/* <form className={classes.root} noValidate autoComplete="off">
                <TextField  required id="standard-required" label="Input the clothing article's url" />
            </form>    */}
      </Box> 
      <div className={classes.backgroundStyle2} > 
       <Box p ={10}> 
        <Grid container spacing={4} >
          <Grid item xs={6} sm={7}>
          <Paper className={classes.paper}>    <Chart /></Paper>
        </Grid>
        <Grid item xs={6} sm={4}>
          <Paper className={classes.paper}> <Table />  </Paper>
          <ChangeLowerBackground/>
        </Grid>
        </Grid>
        </Box>
      </div>

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
    alert('A type was submitted: ' + this.state.value);
    event.preventDefault();
  }

  render() {
    // const { classes } = this.props;
    return (
      <div>
        <form onSubmit={this.handleSubmit} Validate autoComplete="off">
          {/* className={classes.root} */}
            <TextField  value={this.state.value} onChange={this.handleChange} required id="standard-required" label="Clothing Type" />
        </form>
      </div>
    );
  }
}

class ChangeLowerBackground extends React.Component {
  state = {
    open: true
  }

  toggleImage = () => {
    this.setState(state => ({ open: !state.open }))
  }

  getImageName = () => this.state.open ? 'plus' : 'minus'

  render() {
    const imageName = this.getImageName();
    return (
      <div>
        <img style={{maxWidth: '50px'}} src={imagesPath[imageName]} onClick={this.toggleImage} />
      </div>
    );
  }
}

export default App;