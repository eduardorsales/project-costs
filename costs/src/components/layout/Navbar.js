import { Link } from "react-router-dom"

import Container from "./Container"

import styles from './Navbar.module.css'
import logo from '../../img/costs_logo.png'

function Navbar (){
    return(
        <nav className={styles.navbar}>
            <Container>
            <Link to='/'>
                <img src={logo} alt="Logo Costs" />
            </Link>
            <ul className={styles.list}>
                <li className={styles.item}>
                    <Link to='/'>HOME</Link>
                </li>
                <li className={styles.item}>
                    <Link to='/projects'>PROJETOS</Link>
                </li>
                <li className={styles.item}>
                    <Link to='/company'>EMPRESA</Link>
                </li>
                <li className={styles.item}>
                    <Link to='/contact'>CONTATO</Link>
                </li>
            </ul>
            </Container>
        </nav>        
    )
}

export default Navbar