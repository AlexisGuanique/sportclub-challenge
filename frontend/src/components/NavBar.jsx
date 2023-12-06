import { AppBar, Grid, Typography } from "@mui/material"


const NavBar = () => {


    return (
        <AppBar
            position="relative"
            sx={{
                bgcolor: 'white',
                paddingTop: 2
            }}
        >
                <Grid
                    container
                    direction='row'
                    justifyContent='space-between'
                    alignItems='center'
                >
                    <img src="/sportclub.png" alt="Logo" style={{ paddingLeft: 90, marginBottom: 20 }} height="50" />

                    
                    <Typography variant='h6' noWrap component='div' style={{ color: 'black', paddingRight: 80, marginBottom: 20 }}>Sport Club</Typography>
                
                
                </Grid>

        </AppBar>
    )
}

export default NavBar;