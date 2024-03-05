import {FaFacebook, FaInstagram, FaLinkedin} from 'react-icons/fa6'
import styles from './Footer.module.css'

function Footer(){
    return(
        <footer className={styles.footer}>
            <ul className={styles.social_list}>
                <li>
                    <a href='https://www.facebook.com' target='_blanket'> 
                        <FaFacebook />
                    </a>
                </li>
                <li>
                    <a href='https://www.instagram.com' target='_blanket'> 
                        <FaInstagram />
                    </a>
                </li>
                <li> 
                    <a href='https://www.linkedin.com' target='_blanket'>
                    <FaLinkedin />
                    </a>
                </li>
            </ul>
            <p className={styles.copy_right}><span>Costs</span> &copy; 2024</p>
        </footer>
    ) 
}

export default Footer